#!/usr/bin/python3
""" This module is the flask backend to communicate with the web site"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove(response):
    """ calls close method to update storage with flask """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ States list displays in html the state and associated id in the db """
    states = []

    for key, value in storage.all(State).items():
        states.append((value.name, value.id))
    states.sort(key=lambda x: x[0])
    return render_template("9-states.html", zig=2, states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ States displays the state and cities associated with the id """
    states = []
    sig = 0
    for key, value in storage.all(State).items():
        if id == value.id:
            cities = []
            clist = value.cities
            for obj in clist:
                cities.append((obj.name, obj.id))
                cities.sort(key=lambda x: x[0])
            states.append((value.name, value.id, cities))
            sig = 1
            break
    if sig == 1:
        return render_template("9-states.html", zig=3, states=states)
    else:
        return render_template("9-states.html", zig=1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
