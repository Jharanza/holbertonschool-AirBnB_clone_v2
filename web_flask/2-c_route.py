#! /usr/bin/python3
''' Module that create a server that  '''
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def first():
    ''' endpoint root'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def second():
    ''' endpoint that show a string'''
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def third(text):
    ''' endpoint that accept a variable as argument '''
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
