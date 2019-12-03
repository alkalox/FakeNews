from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask'

@app.route('/string')
def stringy():
    return "Baby I win"