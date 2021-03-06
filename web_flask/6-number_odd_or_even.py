#!/usr/bin/python3
""" Program that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
In Routes /: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition
/c/<text>: display “C ” followed by the value of the text variable
/python/<text>: display “Python ”,followed by the value of the text variabl
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer
/number_odd_or_even/<n>: display a HTML page only if n is an integer"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Display a custom String on main Route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display a custom message """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Function that receives a keyword argument and display a message """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': "is_cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Function that receives a keyword argument and display a message
    or a default value """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num_n(n):
    """ Function that receives a number argument and display a message """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ Function that receives a number argument and render the template """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """  Function that receives a number argument, render a template and
    a conditional """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
