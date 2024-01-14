#!/usr/bin/python3
''' module that create a basic server '''
from flask import Flask


app = Flask(__name__)


@app.route('/')
def start():
    ''' Method that show a message'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
