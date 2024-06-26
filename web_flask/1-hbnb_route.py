#!/usr/bin/python3
"""
starts a Flask web application
listens on 0.0.0.0, port 5000
routes: /: display "Hello HBNB!"
/hbnb: display "HBNB"
strict_slashes=False
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays 'Hello HBNB' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays 'HBNB' """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
