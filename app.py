import json
from flask import Flask, jsonify, abort

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True, port=5000) # Run the app on port 5000