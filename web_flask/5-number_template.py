#!/usr/bin/python3
"""
A script that starts a Flask web applicatio
"""

from flask import Flask, render_template
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    display: “python ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>')
def number(n):
    """Return: n is a number if n is int"""
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    display: H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
