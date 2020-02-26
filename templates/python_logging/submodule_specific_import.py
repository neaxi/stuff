#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_logger_message_levels():
    logger.debug('DEBUG level message')
    logger.info('INFO level message')
    logger.warning('WARNING level message')
    logger.error('ERROR level message')
    logger.critical('CRITICAL level message')
    logger.fatal('FATAL level message')

def test_exception():
    try:
        raise ValueError
    except Exception as e:
        logger.exception("The exception has raised")

if __name__ == '__main__':
    test_logger_message_levels()
    test_exception()
