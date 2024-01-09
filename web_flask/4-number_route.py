#! /usr/bin/python3
'''
Module that create a server with a endpoint that receive
a specific type of value
'''
from flask import Flask, render_template, make_response
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    ''' method root of the server '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def second():
    ''' method that returns a message'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def third(text):
    ''' method that returns a variable '''
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    ''' method that returns a variable with a default value '''
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    if isinstance(n, int):
        return f'{escape(n)} is a number'
    else:
        return 'not found'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)