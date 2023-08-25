#!/usr/bin/python3
"""Views for API status and statistics."""

from flask import Blueprint

# Create a Blueprint instance for app_views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the views here to avoid circular imports
from api.v1.views.index import *
