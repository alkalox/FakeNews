from flask import Flask, request, jsonify
from flask_cors import CORS
from prediction import detecting_fake_news

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Flask'

@app.route('/string', methods=['GET'])
def stringy():
    stringy = request.args.get('stringname')
    boolean = detecting_fake_news(stringy)
    result = str(boolean)
    return jsonify(result)