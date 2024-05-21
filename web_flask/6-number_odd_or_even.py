#!/usr/bin/python3
"""
starts a Flask web application
listens on 0.0.0.0, port 5000
routes: /: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C" followed by value of text variable
/python/<text>: display “Python ”, followed by the value of the text
The default value of text is “is cool"
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
	H1 tag: “Number: n” inside the tag BODY
	/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
strict_slashes=False
"""

from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
	""" displays HBNB in route /number/n """
	return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
	""" displays HBNB in route /number/n """
	return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
	""" displays HBNB in route /number/n """
	return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
