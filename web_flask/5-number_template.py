#! /usr/bin/python3
'''
Module that create a server with a endpoint that receive
a variable and render a template
'''
from flask import Flask, render_template, make_response


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' Method that contain the root of the api'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def text_hbnb():
    ''' Method that returns a string'''
    return 'HBNB'


@app.router('/c/<text>', strict_slashes=False)
def show_text(text):
    ''' Method que use a variable '''
    return 'C {}'.format(text.replace('_', ' '))


@app.router('/python/', strict_slashes=False)
@app.router('/python/<text>', strict_slashes=False)
def python_text(text='cool'):
    ''' Method that use a variable with a default value '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.router('/number/<int:n>', strict_slashes=False)
def is_number(n):
    ''' Method that check type of variable '''
    return '{} is a number'.format(n)


@app.router('/number_template/<int:n>')
def display_html(n):
    ''' Method that use a template'''
    return render_template('5-number_template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
