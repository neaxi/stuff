#!/usr/bin/python3
import os

logScreenLevel = 'INFO'
logFileLevel = 'DEBUG'

RUNTIME_LOG = os.path.join(os.path.dirname(__file__), 'last_execution.log')
if not os.path.join(RUNTIME_LOG):
    os.mkdir(RUNTIME_LOG)

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': logScreenLevel,
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': logFileLevel,
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': RUNTIME_LOG,
            'mode': 'w',
        },
    },
    'loggers': {
        '': {
            'level': logFileLevel,
            'handlers': ['default', 'file'],
            'propagate': True
        }
    }
}
