import logging
import subprocess

from util.rpm import is_rpm_installed
from .exceptions import PluginInitError

class adp:
    def __init__(self):
        if not is_rpm_installed('adp'):
            raise PluginInitError('adp is not installed - plugin cannot be initialized')
        logging.info('ADP plugin initialized')

    def run(self):
        try:
            loggging.info('Running ADP plugin')
            subprocess.call(['/usr/sbin/adp-fetch'])
        except Exception as exc:
            logging.error('Error running ADP')
