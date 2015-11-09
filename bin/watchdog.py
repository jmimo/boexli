#!/usr/bin/python3
from daemon import register_shutdown_hook, load_configuration


def main(configuration):
    pass

# https://github.com/lanyonm/ship-it

def shutdown_hook(signum, frame):
    print("cleanup for shutdown")

if __name__ == '__main__':
    register_shutdown_hook(shutdown_hook)
    main(load_configuration())
