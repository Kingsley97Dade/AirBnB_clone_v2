#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_1():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hbnb_2(text):
    text_adj = text.replace("_", " ")
    return "C {}".format(text_adj)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hbnb_3(text):
    text_u = text.replace("_", " ")
    return ("Python {}".format(text_u))


@app.route('/number/<int:n>')
def hbnb_4(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def hbnb_5(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def hbnb_6(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
