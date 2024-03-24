#!/usr/bin/python3
"""
Starts a flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """
    the function serving the root page
    """
    return "Hello HBNB!"


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
