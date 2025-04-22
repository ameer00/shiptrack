import json, time
from flask import Flask, jsonify, abort

# Initialize Flask app
app = Flask(__name__)

@app.route('/discovery', methods=['GET)
def discovery():
    return jsonify({
        "name": "shipping",        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

# create liveness and readiness endpoints
@app.route('/liveness', methods=['GET'])
def liveness():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

@app.route('/readiness', methods=['GET'])
def readiness():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})
    

if __name__ == '__main__':
    app.run(debug=True) # Run the Flask development server