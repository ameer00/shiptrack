import json
import time
import requests
from flask import Flask, jsonify, request, abort
from backend_handlers import discovery

app = Flask(__name__)

# create the discovery, liveness and readiness endpoints
@app.route('/discovery', methods=['GET'])
def discovery_route():
    return discovery()

@app.route('/live', methods=['GET'])
def liveness_route():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

@app.route('/ready', methods=['GET'])
def readiness_route():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
