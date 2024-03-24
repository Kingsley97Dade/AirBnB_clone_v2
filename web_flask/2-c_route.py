#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_1():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hbnb_2(text):
    text_adj = text.replace("_", " ")
    return "C {}".format(text_adj)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
