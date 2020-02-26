# Absolute basic set-up
# 1. import the library
# 2. set more descriptive message format and a minimal logging level
# 3. instantiate logger
# 4. test the messages


# just put these three lines in all your scripts
import logging
logging.basicConfig(format='[%(levelname)s] %(name)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)



logger.debug('DEBUG level message')
logger.info('INFO level message')
logger.warning('WARNING level message')
logger.error('ERROR level message')
logger.critical('CRITICAL level message')
logger.fatal('FATAL level message')