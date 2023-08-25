#!/usr/bin/python3
"""index"""
from api.v1.views import app_views

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def api_stats():
    """Return statistics about data objects."""
    statistics = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(statistics)


@app_views.route("/status")
def api_status():
    """Return API status."""
    return {"status": "OK"}
