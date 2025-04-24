import json
import os
import time
from flask import Flask, jsonify, abort

# Initialize Flask app
app = Flask(__name__)

@app.route('/discovery', methods=['GET'])
def discovery():
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

# create liveness and readiness endpoints
@app.route('/readiness', methods=['GET'])
def readiness():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})

@app.route('/liveness', methods=['GET'])
def liveness():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

PACKAGES_FILE = 'packages.json'

def load_packages():
    """Load packages from the JSON file."""
    try:
        with open(PACKAGES_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

packages = load_packages()

@app.route('/packages/<package_id>', methods=['GET'])
def get_package(package_id):
    """Retrieve a package by its ID."""
    for package in packages:
        if package['packageId'] == package_id:
            return jsonify(package)
    abort(404, description=json.dumps({"code": "NOT_FOUND", "message": f"Package with ID {package_id} not found."}))
    

if __name__ == '__main__':
    app.run(debug=True) # Run the Flask development server