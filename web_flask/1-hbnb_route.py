#!/usr/bin/python3
"""
A script that starts a Flask web applicatio
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    display "Hello HBNB!" at 0.0.0.0:5000/
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display “HBNB” at 0.0.0.0:5000/
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
