#!/usr/bin/python3
from daemon import register_shutdown_hook, load_configuration
from flask import Flask, request
from flask_restful import Resource, Api, abort
import RPi.GPIO as GPIO


class Led(Resource):

    def get(self, state):
        if state == 'red':
            red()
        elif state == 'green':
            green()
        elif state == 'orange':
            orange()
        elif state == 'off':
            off()
        else:
            off()
            abort(400, message='unknown color: {}'.format(color))



def prepare_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)


def red():
    off()
    GPIO.output(11, True)


def green():
    off()
    GPIO.output(7, True)


def orange():
    off()
    GPIO.output(7, True)
    GPIO.output(11, True)


def off():
    GPIO.output(7, False)
    GPIO.output(11, False)


def cleanup_gpio():
    GPIO.cleanup()


def main():
    prepare_gpio()
    app = Flask(__name__)

    api = Api(app)
    #api.add_resource(Led, '/led/<string:state>')
    api.add_resource(Led, '/led/<string:state>')

    app.run(host='0.0.0.0', port=80, debug=True)


def shutdown_hook(signum, frame):
    print("cleanup for shutdown")
    cleanup_gpio()

if __name__ == '__main__':
    register_shutdown_hook(shutdown_hook)
    main()


