#!/usr/bin/python3
''' Module that display the States from DBStorage '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask('__name__')


@app.route('/')
def hello():
    return 'Hello Jhony'


@app.teardown_appcontext()
def teardown_session(exception):
    ''' Method that close the session '''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_and_states():
    ''' Method that  '''
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
