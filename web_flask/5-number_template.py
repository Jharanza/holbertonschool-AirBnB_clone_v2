#! /usr/bin/python3
'''
Module that create a server with a endpoint that receive
a variable and render a template
'''
from flask import Flask, render_template, make_response


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def text_hbnb():
    return 'HBNB'


@app.router('/c/<text>', strict_slashes=False)
def show_text(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.router('/python/', strict_slashes=False)
@app.router('/python/<text>', strict_slashes=False)
def python_text(text='cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.router('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return '{} is a number'.format(n)


@app.router('/number_template/<int:n>')
def display_html(n):
    return render_template('5-number_template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
