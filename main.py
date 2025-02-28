import json, time, requests
from flask import Flask, jsonify, request, abort
from data_model import Package
from connect_connector import SessionMaker


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

# liveness and readiness routes
@app.route('/live', methods=['GET'])
def liveness():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

@app.route('/ready', methods=['GET'])
def readiness():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
