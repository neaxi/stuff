#!/usr/bin/python3
import os

# CONSTANTS
log_level_screen = 'INFO'
log_level_file = 'DEBUG'
log_filename = 'last_execution.log'
date_format = '%Y-%m-%dT%H:%M:%S%z'    # ISO 8601!!!


# Checks for writing a logfile
RUNTIME_LOG = os.path.join(os.path.dirname(__file__), log_filename)

# check if the path where we want to store the file exists, create subfolders otherwise
if not os.path.exists(os.path.dirname(RUNTIME_LOG)):
    os.makedirs(os.path.dirname(RUNTIME_LOG))
# check if the name doesn't already exists as a dir
if os.path.isdir(RUNTIME_LOG):
    raise Exception('Log path is not a file but a directory: {}'.format(RUNTIME_LOG))


DEFAULT_LOGGING = {
    'version': 1,
    # disable_existing_loggers – If specified as False, loggers which exist when this call is made are left enabled.
    'disable_existing_loggers': False,  
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s',
            'datefmt': date_format
        },
        'extensive': {
            # all available attributes - https://docs.python.org/3/library/logging.html#logrecord-attributes
            'format': '[%(asctime)s] [PID:%(process)d TID:%(thread)d] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s',
            'datefmt': date_format
        }
    },
    'loggers': {
         # Optional levels for specific imports/libraries;
         # Useful when some of the imported libraries is too talkative
         # submodule_specific_import.py
         'submodule_specific_import': {
             'level': 'INFO',
             'handlers': ['stdio_extensive'],
             # propagate attribute is True for a Logger instance by default
             'propagate': False
         },
        '': {
            'level': log_level_file,
            'handlers': ['stdio_default', 'file'],
        },
    },    
    'handlers': {
        'stdio_default': {
            'level': log_level_screen,
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'stdio_extensive': {
            'level': log_level_screen,
            'formatter': 'extensive',
            'class': 'logging.StreamHandler',
        },        
        'file': {
            'level': log_level_file,
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': RUNTIME_LOG,
            # 'a' = append 
            # 'w' = write, overwrites current content
            'mode': 'w',
        },
# If we want to have multiple FileHandlers, they must be 'append'.
# Otherwise they would overwrite logs from previous FileHandler.
# Handlers are not running in parallel && aren't process safe ==> AVOID!!
# details https://realpython.com/python-logging-source-code/#preliminary-2-logging-is-thread-safe-but-not-process-safe
#        'file_extensive': {
#            'level': log_level_screen,
#            'formatter': 'extensive',
#            'class': 'logging.FileHandler',
#            'filename': RUNTIME_LOG,
#            'mode': 'a'
#        }
    }
}
