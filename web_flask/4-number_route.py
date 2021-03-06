#!/usr/bin/python3
""" This module is the flask backend to communicate with the web site"""

from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ index is the html home page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ the hbnb web page """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ define your url """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """ python (is cool) """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """ display n only if integer """
    try:
        return "{} is a number".format(int(n))
    except:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
