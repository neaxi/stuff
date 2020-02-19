#!/usr/bin/python3

# basic setup without any external logger, to make sure we're processing everything by default
from logging import DEBUG, basicConfig, getLogger
basicConfig(format='%(name)s: %(message)s', level=DEBUG)
logger = getLogger(__name__)

def test_logger_message_levels():
    logger.debug('DEBUG level message')
    logger.info('INFO level message')
    logger.warning('WARNING level message')
    logger.error('ERROR level message')
    logger.critical('CRITICAL level message')
    logger.fatal('FATAL level message')

def main():
    test_logger_message_levels()

if __name__ == '__main__':
    main()
