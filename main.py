import json, time, requests
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

def discovery():
    """
    Returns the discovery information for the shiptrack service.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

# Add the route for the discovery endpoint
app.add_url_rule('/discovery', 'discovery', discovery, methods=['GET'])

@app.route('/liveness', methods=['GET'])
def liveness():
    """
    Returns the liveness status of the shiptrack service.
    """
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})


if __name__ == '__main__':
    app.run(debug=True)
