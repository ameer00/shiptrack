import json, time, requests
from flask import Flask, jsonify, request, abort

app = Flask(__name__)


@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Discovery API endpoint.

    Returns:
        JSON response containing the service's name, version, owners, team, and organization.
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
    Liveness API endpoint.

    Returns:
        JSON response indicating the service's liveness status.
    """
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})


if __name__ == '__main__':
    app.run(debug=True)
