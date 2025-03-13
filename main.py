import json
import time
import requests
from flask import Flask, jsonify, request, abort
from backend_handlers import discovery

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
