#
# GPOA - GPO Applier for Linux
#
# Copyright (C) 2019-2020 BaseALT Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import gettext

def info_code(code):
    info_ids = dict()
    info_ids[1] = 'Got GPO list for username'
    info_ids[2] = 'Got GPO'

    return info_ids.get(code, 'Unknown info code')

def error_code(code):
    error_ids = dict()
    error_ids[1] = 'Insufficient permissions to run gpupdate'
    error_ids[2] = 'gpupdate will not be started'
    error_ids[3] = 'Backend execution error'
    error_ids[4] = 'Error occurred while running frontend manager'
    error_ids[5] = 'Error running GPOA for computer'
    error_ids[6] = 'Error running GPOA for user'
    error_ids[7] = 'Unable to initialize Samba backend'
    error_ids[8] = 'Unable to initialize no-domain backend'
    error_ids[9] = 'Error running ADP'
    error_ids[10] = 'Unable to determine DC hostname'
    error_ids[11] = 'Error occured while running applier with user privileges'
    error_ids[12] = 'Unable to initialize backend'
    error_ids[13] = 'Not sufficient privileges to run machine appliers'
    error_ids[14] = 'Kerberos ticket check failed'
    error_ids[15] = 'Unable to retrieve domain name via CLDAP query'
    error_ids[16] = 'Error getting SID using wbinfo, will use SID from cache'
    error_ids[17] = 'Unable to get GPO list for user from AD DC'
    error_ids[18] = 'Error getting XDG_DESKTOP_DIR'
    error_ids[19] = 'Error occured while running user applier in administrator context'
    error_ids[20] = 'Error occured while running user applier in user context (with dropped privileges)'
    error_ids[21] = 'No reply from oddjobd GPOA runner via D-Bus for current user'
    error_ids[22] = 'No reply from oddjobd GPOA runner via D-Bus for computer'
    error_ids[23] = 'No reply from oddjobd GPOA runner via D-Bus for user'
    error_ids[24] = 'Error occured while running machine applier'
    error_ids[25] = 'Error occured while initializing user applier'
    error_ids[26] = 'Error merging machine GPT'
    error_ids[27] = 'Error merging user GPT'
    error_ids[28] = 'Error merging machine part of GPT'
    error_ids[29] = 'Error merging user part of GPT'

    return error_ids.get(code, 'Unknown error code')

def debug_code(code):
    debug_ids = dict()
    debug_ids[1] = 'The GPOA process was started for user'
    debug_ids[2] = 'Username is not specified - will use username of the current process'
    debug_ids[3] = 'Initializing plugin manager'
    debug_ids[4] = 'ADP plugin initialized'
    debug_ids[5] = 'Running ADP plugin'
    debug_ids[6] = 'Starting GPOA for user via D-Bus'
    debug_ids[7] = 'Cache directory determined'
    debug_ids[8] = 'Initializing local backend without domain'
    debug_ids[9] = 'Initializing Samba backend for domain'
    debug_ids[10] = 'Group Policy target set for update'
    debug_ids[11] = 'Starting GPOA for computer via D-Bus'
    debug_ids[12] = 'Got exit code'
    debug_ids[13] = 'Starting GPOA via D-Bus'
    debug_ids[14] = 'Starting GPOA via command invocation'
    debug_ids[15] = 'Username for frontend is determined'
    debug_ids[16] = 'Applying computer part of settings'
    debug_ids[17] = 'Kerberos ticket check succeed'
    debug_ids[18] = 'Found AD domain via CLDAP query'
    debug_ids[19] = 'Setting info'
    debug_ids[20] = 'Initializing cache'
    debug_ids[21] = 'Set operational SID'
    debug_ids[22] = 'Got PReg entry'
    debug_ids[23] = 'Looking for preference in user part of GPT'
    debug_ids[24] = 'Looking for preference in machine part of GPT'
    debug_ids[25] = 'Re-caching Local Policy'
    debug_ids[26] = 'Adding HKCU entry'
    debug_ids[27] = 'Skipping HKLM branch deletion key'
    debug_ids[28] = 'Reading and merging machine preference'
    debug_ids[29] = 'Reading and merging user preference'
    debug_ids[30] = 'Found SYSVOL entry'
    debug_ids[31] = 'Trying to load PReg from .pol file'
    debug_ids[32] = 'Finished reading PReg from .pol file'
    debug_ids[33] = 'Determined length of PReg file'
    debug_ids[34] = 'Merging machine settings from PReg file'
    debug_ids[35] = 'Merging machine (user part) settings from PReg file'
    debug_ids[36] = 'Loading PReg from XML'
    debug_ids[37] = 'Setting process permissions'
    debug_ids[38] = 'Samba DC setting is overriden by user setting'
    debug_ids[39] = 'Saving information about drive mapping'
    debug_ids[40] = 'Saving information about printer'
    debug_ids[41] = 'Saving information about link'
    debug_ids[42] = 'Saving information about folder'
    debug_ids[43] = 'No value cached for object'
    debug_ids[44] = 'Key is already present in cache, will update the value'
    debug_ids[45] = 'GPO update started'
    debug_ids[46] = 'GPO update finished'
    debug_ids[47] = 'Retrieving list of GPOs to replicate from AD DC'
    debug_ids[48] = 'Establishing connection with AD DC'
    debug_ids[49] = 'Started GPO replication from AD DC'
    debug_ids[50] = 'Finished GPO replication from AD DC'
    debug_ids[51] = 'Skipping HKCU branch deletion key'
    debug_ids[52] = 'Read domain name from configuration file'
    debug_ids[53] = 'Saving information about environment variables'

    return debug_ids.get(code, 'Unknown debug code')

def warning_code(code):
    warning_ids = dict()
    warning_ids[1] = (
        'Unable to perform gpupdate for non-existent user, '
        'will update machine settings'
    )
    warning_ids[2] = (
        'Current permissions does not allow to perform gpupdate for '
        'designated user. Will update current user settings'
    )
    warning_ids[3] = 'oddjobd is inaccessible'
    warning_ids[4] = 'No SYSVOL entry assigned to GPO'
    warning_ids[5] = 'ADP package is not installed - plugin will not be initialized'

    return warning_ids.get(code, 'Unknown warning code')

def fatal_code(code):
    fatal_ids = dict()
    fatal_ids[1] = 'Unable to refresh GPO list'
    fatal_ids[2] = 'Error getting GPTs for machine'
    fatal_ids[3] = 'Error getting GPTs for user'

    return fatal_ids.get(code, 'Unknown fatal code')

def get_message(code):
    retstr = 'Unknown message type, no message assigned'

    if code.startswith('E'):
        retstr = error_code(int(code[1:]))
    if code.startswith('I'):
        retstr = info_code(int(code[1:]))
    if code.startswith('D'):
        retstr = debug_code(int(code[1:]))
    if code.startswith('W'):
        retstr = warning_code(int(code[1:]))
    if code.startswith('F'):
        retstr = fatal_code(int(code[1:]))

    return retstr

def message_with_code(code):
    retstr = '[' + code[0:1] + code[1:].rjust(5, '0') + ']| ' + gettext.gettext(get_message(code))

    return retstr

