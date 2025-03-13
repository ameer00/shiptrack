import json, time, requests
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Provides information about the Shiptrack service.

    Returns:
        JSON: A JSON object containing the service's name, version, owners, team, and organization.
    """
    return jsonify({
        "name": "shiptrack",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

@app.route('/liveness', methods=['GET'])
def liveness():
    """
    Checks the liveness status of the Shiptrack    service.

    Returns:
        JSON: A JSON object indicating the service's status, code, and timestamp.
    """
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

@app.route('/readiness', methods=['GET'])
def readiness():
    """
    Checks the readiness status of the Shiptrack service.

    Returns:
        JSON: A JSON object indicating the service's status, code, and timestamp.
    """
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
