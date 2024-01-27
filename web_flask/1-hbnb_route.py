#!/usr/bin/python3
"""start a simple Flask web application"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
