#!/usr/bin/python3
from daemon import register_shutdown_hook, load_configuration
from flask import Flask, request
from flask_restful import Resource, Api, abort
import RPi.GPIO as GPIO


class Led(Resource):

    def get(self, state, color):
        if state == 'on':
            if color == 'red':
                red()
            elif color == 'green':
                green()
            elif color == 'orange':
                orange()
            else:
                abort(400, message='unknown color: {}'.format(color))
        elif state == 'off':
            off()
        else:
            abort(400, message='unknown state: {}'.format(state))



def prepare_gpio():
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
    api.add_resource(Led, '/led/<string:state>')
    api.add_resource(Led, '/led/<string:state>/<string:color>')

    app.run(debug=True)


def shutdown_hook(signum, frame):
    print("cleanup for shutdown")
    cleanup_gpio()

if __name__ == '__main__':
    register_shutdown_hook(shutdown_hook)
    main(load_configuration())


