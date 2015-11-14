from datetime import datetime
from sys import exit
from signal import signal, SIGTERM
import ConfigParser
from os.path import isfile
import argparse


def get_now():
    "get the current date and time as a string"
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def shutdown_handler(signum, frame):
    '''
    will exit the application.
    '''
    print "[" + get_now() + "] received signal {}, exiting...".format(_signo)
    exit(0)


def register_shutdown_hook(shutdown_hook):
    '''
    :param shutdown_hook: function executed when sigterm is received. The function
    needs to contain the following signature: (signum, frame)
    '''
    signal(SIGTERM, shutdown_hook)
    signal(SIGTERM, shutdown_handler)


def parse_input():
    parser = argparse.ArgumentParser(description='Generic service arguments')
    parser.add_argument('configuration', required=True, type=str, help='path to python style configuration file.')
    return parser.parse_args()


def load_configuration():
    arguments = parse_input()
    if not isfile(arguments.configuration):
        raise FileNotFoundError
    config = ConfigParser.RawConfigParser()
    config.read(arguments.configuration)
    return config

