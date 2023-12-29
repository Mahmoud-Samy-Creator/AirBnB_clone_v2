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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    display: “python ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<n>", strict_slashes=False)
def n_is_num(n):
    """
    display “n is a number” only if n is an integer
    """
    number = float(n)
    message = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server.  \
        If you entered the URL manually please check your spelling and try again.</p>
              """
    if number.is_integer():
        return f"{escape(int(number))} is a number"
    else:
        return message


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
