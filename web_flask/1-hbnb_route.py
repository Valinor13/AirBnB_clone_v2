#!/usr/bin/python3
""" This module is the flask backend to communicate with the web site"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ index is the html home page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ the hbnb web page """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
