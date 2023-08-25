#!/usr/bin/python3
"""Routes for API status and statistics."""

from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place


# Route for API status
@app_views.route('/status', strict_slashes=False)
def api_status():
    """Return API status."""
    return jsonify(status="OK")

# Route for statistics
@app_views.route('/stats', strict_slashes=False)
def api_stats():
    """Return statistics about data objects."""
    statistics = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(statistics)
