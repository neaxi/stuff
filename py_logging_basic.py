# loggingSetup.py

logLevel = 'INFO'

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            #'format': '[%(asctime)s] [PID:%(process)d TID:%(thread)d] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s'
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': logLevel,
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'level': logLevel,
            'handlers': ['default'],
            'propagate': True
        }
logLevel = 'INFO'

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            #'format': '[%(asctime)s] [PID:%(process)d TID:%(thread)d] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s'
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': logLevel,
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'level': logLevel,
            'handlers': ['default'],
            'propagate': True
        }
logLevel = 'INFO'

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            #'format': '[%(asctime)s] [PID:%(process)d TID:%(thread)d] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s'
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': logLevel,
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'level': logLevel,
            'handlers': ['default'],
            'propagate': True
        }
#===============================================================================
#         ,
#         # Optional levels for specific libraries
#         'requests.packages.urllib3.connectionpool': {
#             'level': 'ERROR',
#             'handlers': ['default'],
#             'propagate': True
#         }
#===============================================================================
    }
}




# main.py
import logging.config
import click
#from loggingSetup import DEFAULT_LOGGING

logging.basicConfig()
logging.config.dictConfig(DEFAULT_LOGGING)
logger = logging.getLogger(__name__)

@click.command()
@click.option('--debug', is_flag=True, help='Turns on debug level logs')
def main(debug):
    if debug:
        global logger
        logger = logging.getLogger()
        logging.getLogger().setLevel(logging.DEBUG)
        logger.handlers[0].setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s'))
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)
        logging.info('Debug mode turned ON!')

        
    logger.info('Test info message')
    logger.debug('Test debug message')
        
if __name__ == "__main__":
    main()
