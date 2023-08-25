#!/usr/bin/python3
"""Routes for API status and statistics."""

from flask import jsonify
from api.v1.views import app_views

# Route for API status
@app_views.route('/status', strict_slashes=False)
def api_status():
    """Return API status."""
    return jsonify(status="OK")
