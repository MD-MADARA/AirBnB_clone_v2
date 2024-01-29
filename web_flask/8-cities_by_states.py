#!/usr/bin/python3
"""start a simple Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


# Register a function to be called when the application context is torn down
@app.teardown_appcontext
def teardown_session(exception=None):
    """close the session"""
    storage.close()


@app.route('/states_list')
def list_states():
    """Display states list"""
    res = storage.all(State).values()
    # storage.all(State) is dictionary of states object
    return render_template('7-states_list.html', states=res)


@app.route('/cities_by_states')
def cities_by_state():
    """Display kist of cities by state"""
    res = storage.all(State).values()
    # storage.all(State) is dictionary of states object
    return render_template('8-cities_by_states.html', states=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
