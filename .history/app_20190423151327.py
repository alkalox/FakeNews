from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Flask'

@app.route('/string', methods=['GET'])
def stringy():
    stringy = request.args.get('stringname')
    return stringy.json()