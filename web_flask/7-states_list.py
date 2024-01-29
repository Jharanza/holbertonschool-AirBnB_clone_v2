#!/usr/bin/python3
''' Module that fetch data from storage engine '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exc):
    ''' Method that close the session '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    ''' Method that list all states sorted bt name '''
    states = storage.all(State).values()
    states = sorted(states,  key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
