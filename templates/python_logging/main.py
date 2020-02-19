#!/usr/bin/python3

import submodule_x
import submodule_specific_import
import setup_cli_args

import logging.config 
from setup_logging import DEFAULT_LOGGING

# ARGUMENT PARSER SETUP - to know args/flags/--debug prior setting up logging
parser = setup_cli_args.setup_parser()
args = parser.parse_args()

# LOGGER SETUP
logging.basicConfig()    # create default root logger
logging.config.dictConfig(DEFAULT_LOGGING)    # load configuration
logging.getLogger().handlers[0].setLevel(args.log_level)    # console logger handler is set to level dictated by CLI args
logger = logging.getLogger(__name__)






logger.info('App started')
logger.debug('Debugging mode turned on')
logger.info('Testing message levels:\n'+'-'*50)

# the reason we're calling the test from a submodule is that we want to check
# that the logger setting is properly propagated also to imported libraries
submodule_x.test_logger_message_levels()


logger.info('\n'+'-'*50)
logger.debug('Second round with more detailed/extensive log applied on specific import')
logger.info('Testing message levels.. round 2:\n'+'-'*50)
submodule_specific_import.test_logger_message_levels()