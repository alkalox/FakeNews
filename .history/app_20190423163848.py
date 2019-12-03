from flask import Flask, request, jsonify
from flask_cors import CORS
from prediction import predict_fake_news

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Flask'

@app.route('/string', methods=['GET'])
def stringy():
    stringy = request.args.get('stringname')
    return jsonify(stringy)