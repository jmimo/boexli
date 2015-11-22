#!/usr/bin/python
from daemon import register_shutdown_hook, load_configuration


def main(config):
    pass
    # TODO observe GPS
    # TODO observe pressure
    # TODO signal system status via output service

def shutdown_hook(signum, frame):
    print "cleanup for shutdown"
    cleanup_gpio()

if __name__ == '__main__':
    register_shutdown_hook(shutdown_hook)
    main(load_configuration())


