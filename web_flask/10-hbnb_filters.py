#!/usr/bin/python3
"""start a simple Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


# Register a function to be called when the application context is torn down
@app.teardown_appcontext
def teardown_session(exception=None):
    """close the session"""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Display kist of cities by state"""
    sts = storage.all(State).values()
    ams = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=sts, amenities=ams)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
