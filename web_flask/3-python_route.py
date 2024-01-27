#!/usr/bin/python3
"""start a simple Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def Hello_HBNB():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def Hbnb():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """Display variable"""
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """Display variable"""
    return f"Python {escape(text).replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
