#!/usr/bin/python3
""" This module is the flask backend to communicate with the web site"""

from flask import Flask, abort, redirect, url_for, render_template

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
        int(n)
        return render_template("template/5-number.html", number=n)
    except:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """ display n only if integer """
    try:
        return render_template("5-number.html", number=int(n))
    except:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    """ displays n and odd or even status only if int """
    try:
        if int(n) % 2 == 0:
            status = "even"
        else:
            status = "odd"
        return render_template("6-number_odd_or_even.html",
                               number=n,
                               status=status)
    except:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
