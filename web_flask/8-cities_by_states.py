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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ States list displays in html the state and associated id in the db """
    states = []
    for key, value in storage.all(State).items():
        cities = []
        clist = value.cities
        for obj in clist:
            cities.append((obj.name, obj.id))
            cities.sort(key=lambda x: x[0])
        states.append((value.name, value.id, cities))
    states.sort(key=lambda x: x[0])

    return render_template("8-cities_by_states.html", states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
