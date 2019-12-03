from .cache import cache

import logging
import os

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData
)
from sqlalchemy.orm import (
    mapper,
    sessionmaker
)


def mapping_factory(mapper_suffix):
    exec(
        '''
class mapped_id_{}(object):
    def __init__(self, str_id, value):
        self.str_id = str_id
        self.value = str(value)
        '''.format(mapper_suffix)
    )
    return eval('mapped_id_{}'.format(mapper_suffix))

class sqlite_cache(cache):
    __cache_dir = 'sqlite:////var/cache/samba'

    def __init__(self, cache_name):
        self.cache_name = cache_name
        self.mapper_obj = mapping_factory(self.cache_name)
        self.storage_uri = os.path.join(self.__cache_dir, '{}.sqlite'.format(self.cache_name))
        logging.debug('Initializing cache {}'.format(self.storage_uri))
        self.db_cnt = create_engine(self.storage_uri, echo=False)
        self.__metadata = MetaData(self.db_cnt)
        self.cache_table = Table(
            self.cache_name,
            self.__metadata,
            Column('id', Integer, primary_key=True),
            Column('str_id', String(65536), unique=True),
            Column('value', String)
        )

        self.__metadata.create_all(self.db_cnt)
        Session = sessionmaker(bind=self.db_cnt)
        self.db_session = Session()
        mapper(self.mapper_obj, self.cache_table)

    def store(self, str_id, value):
        obj = self.mapper_obj(str_id, value)
        self._upsert(obj)

    def get(self, obj_id):
        result = self.db_session.query(self.mapper_obj).filter(self.mapper_obj.str_id == obj_id).first()
        return result

    def get_default(self, obj_id, default_value):
        result = self.get(obj_id)
        if result == None:
            logging.debug('No value cached for {}'.format(obj_id))
            self.store(obj_id, default_value)
            return str(default_value)
        return result.value

    def _upsert(self, obj):
        try:
            self.db_session.add(obj)
            self.db_session.commit()
        except:
            self.db_session.rollback()
            logging.error('Error inserting value into cache, will update the value')
            self.db_session.query(self.mapper_obj).filter(self.mapper_obj.str_id == obj.str_id).update({ 'value': obj.value })
            self.db_session.commit()
