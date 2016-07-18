from ConfigParser import ConfigParser
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILENAME = '.env'


def get_credentials(filename=os.path.join(ROOT_DIR, CREDENTIALS_FILENAME)):
    config_parser = ConfigParser()
    config_parser.read(filename)
    return config_parser
