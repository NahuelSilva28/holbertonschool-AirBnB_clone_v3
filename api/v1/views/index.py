#!/usr/bin/python3
"""index"""
from api.v1.views import app_views

@app_views.route("/status")
def api_status():
    """Return API status."""
    return {"status": "OK"}
