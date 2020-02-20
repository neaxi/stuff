#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG)

def test_logger_message_levels():
    logging.debug('DEBUG level message')
    logging.info('INFO level message')
    logging.warning('WARNING level message')
    logging.error('ERROR level message')
    logging.critical('CRITICAL level message')
    logging.fatal('FATAL level message')

def test_exception():
    try:
        raise ValueError
    except Exception as e:
        logging.exception("The exception has raised")

if __name__ == '__main__':
    test_logger_message_levels()
    test_exception()
