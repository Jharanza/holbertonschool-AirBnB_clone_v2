#! /usr/bin/python3
''' Module that create a server with two points '''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def first():
    ''' Method root '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def second():
    ''' Method that redirection to another point '''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
