from flask import Flask, jsonify, request, abort
import json, time
import requests  # Import the requests library

app = Flask(__name__)

# --- Discovery API Backend Route ---
def discovery():
    """
    Provides information about the shipping service.
    This is the implementation of the Discovery API backend route.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

app.add_url_rule('/discovery', 'discovery', discovery, methods=['GET'])
# --- End of Discovery API ---

@app.route('/liveness', methods=['GET'])
def liveness():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

# ccreate the readiness backend route
@app.route('/readiness', methods=['GET'])
def readiness():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
