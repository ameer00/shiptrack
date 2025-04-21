import json
from flask import Flask, jsonify, abort
import os, time

# --- Flask App ---
app = Flask(__name__)

# --- Discovery Endpoint ---
@app.route('/discovery', methods=['GET'])
def discovery():
    """Returns metadata about the service."""
    return jsonify({
        "name": "shipping", # Service name
        "version": "1.0",   # Service version
        "owners": ["ameerabb", "lonestar"], # Owners of the service
        "team": "genAIs",   # Team responsible for the service
        "organization": "acme" # Organization the service belongs to
    })

@app.route('/liveness', methods=['GET'])
def liveness():
    """Returns the liveness status of the service."""
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

# create the readiness endpoint
@app.route('/readiness', methods=['GET'])
def readiness():
    """Returns the readiness status of the service."""
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask development server