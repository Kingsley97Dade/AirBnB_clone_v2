#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_1():
    return "HBNB"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
