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


@app.route('/states')
@app.route('/states/<id>')
def state_by_id(id=None):
    """Display kist of cities by state"""
    res = storage.all(State).values()
    # storage.all(State) is dictionary of states object
    if id is None:
        return render_template('7-states_list.html', states=res)
    for state in res:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
