from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask'

@app.route('/string', methods=['GET'])
def stringy(stringy):
    stringy = request.args.get('stringname') #if key doesn't exist, returns None
    return stringy