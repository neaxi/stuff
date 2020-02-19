#!/usr/bin/python3
import os

log_screen_level = 'INFO'
log_file_level = 'DEBUG'
date_format = '%Y-%m-%dT%H:%M:%S%z'    # ISO 8601!!!


RUNTIME_LOG = os.path.join(os.path.dirname(__file__), 'last_execution.log')
if not os.path.join(RUNTIME_LOG):
    os.mkdir(RUNTIME_LOG)

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
    'handlers': {
        'default': {
            'level': log_screen_level,
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': log_file_level,
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': RUNTIME_LOG,
            'mode': 'w',
        },
        'default_extensive': {
            'level': log_screen_level,
            'formatter': 'extensive',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'level': log_file_level,
            'handlers': ['default', 'file'],
            'propagate': True
        },
         # Optional levels for specific imports/libraries; 
         # submodule_specific_import.py
         'submodule_specific_import': {
             'level': 'ERROR',
             'handlers': ['default_extensive'],
             #'propagate': True
         }
    }
}
