#!/usr/bin/python3
"""
starts a Flask web application
listens on 0.0.0.0, port 5000
routes: /: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C" followed by value of text variable
/python/<text>: display “Python ”, followed by the value of the text
The default value of text is “is cool"
strict_slashes=False
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB in route /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ displays HBNB in route /hbnb """
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False, defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ displays HBNB in route /hbnb """
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
