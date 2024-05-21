#!/usr/bin/python3
"""
starts a Flask web application
listens on 0.0.0.0, port 5000
routes: /: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C" followed by value of text variable
strict_slashes=False
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays "Hello HBNB" """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays "HBNB" """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ displays c text"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
