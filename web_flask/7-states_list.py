#!/usr/bin/python3
""" This module is the flask backend to communicate with the web site"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ States list displays in html the state and associated id in the db """
    slist = []

    for key, value in storage.all(State).items():
        slist.append((value.name, value.id))
    slist.sort(key = lambda x: x[0])
    return  render_template("7-states_list.html", slist=slist)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
