#!/usr/bin/python3
"""Main module for the API"""


from api.v1.views import app_views
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage

# Flask instance
app = Flask(__name__)

# Register the blueprint for API views
app.register_blueprint(app_views)

# Allow cross-origin requests
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


# Close database
@app.teardown_appcontext
def close_db(error):
    """Close the database connection after each request."""
    storage.close()


# Run the app if executed directly
if __name__ == "__main__":
    import os
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    app.run(host=host, port=port, threaded=True)
