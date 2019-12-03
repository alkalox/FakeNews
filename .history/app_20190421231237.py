from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask'

@app.route('/string')
def stringy():
    stringname = request.args.get('stringname') #if key doesn't exist, returns None
    if stringname == None:
        return '''<h1> </h1>'''
    return '''<h1>The stringname value is: {}</h1>'''.format(stringname)