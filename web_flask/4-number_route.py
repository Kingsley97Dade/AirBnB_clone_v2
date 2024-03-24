#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """
    the function serving the root page
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    the function serving the hbnb page
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    the function displaying /c/<text>
    """
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    the function displaying /python/<text>>
    """
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_only(n):
    """
    the function displaying number only
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    """
    Run the application when the script is executed directly.

    This block of code is executed only if the Python script is run
    directly, not imported as a module. It starts the Flask application,
    allowing it to be accessed externally.
    """

    Usage:
        0-hello_route.py

    Args:
        host (str): The IP address to bind the Flask application to.
                    Defaults to "0.0.0.0" to allow external access.
        port (int): The port number to run the Flask application on.
                    Defaults to 5000.
    
    app.run(host="0.0.0.0", port=5000)
