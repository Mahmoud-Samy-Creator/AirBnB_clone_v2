#!/usr/bin/python3
"""
A script that starts a Flask web applicatio
"""

from flask import Flask
from markupsafe import escape

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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    display: “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
