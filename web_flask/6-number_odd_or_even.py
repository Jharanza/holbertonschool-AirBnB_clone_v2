#! /usr/bin/python3
'''
Module that create a server with a endpoint that receive
2 variables and render a template that change with the value of
the variable
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' Endpoint root of the server '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def text_hbnb():
    ''' Endpoint that return a string '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    ''' Endpoint that return a variable '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='cool'):
    ''' Endpoint that returns a variable with a default value '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    ''' Endpoint with a variable that confirms is a number '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def display_html(n):
    ''' Endpoint that render a template '''
    return render_template('number_template.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    ''' endpoint that render a template with 2 variables '''
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_even='even' if n % 2 == 0 else 'odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
