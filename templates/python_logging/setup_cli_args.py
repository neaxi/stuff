from argparse import ArgumentParser
from logging import DEBUG, INFO, basicConfig, getLogger

basicConfig(format='%(name)s: %(message)s', level=DEBUG)
logger = getLogger(__name__)


def setup_parser():
    '''
    Basic setup for Argparse. 
    Whatever CLI behavior needs to be changes, it's done here on the side outside of the main application.
    '''
    parser = ArgumentParser()

    parser.add_argument(
        '-d', '--debug',
        help='Turns on DEBUG level logging',
        action='store_const', dest='log_level', const=DEBUG,
        default=INFO,
    )
    
    return parser 

