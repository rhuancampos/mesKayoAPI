#!flask/bin/python
from flask import Flask, request
from apiKayo import apiKayo
import gc
import os
import json
import numpy

app = Flask(__name__)

def convert(o):
    if isinstance(o, numpy.int64): return int(o)  
    raise TypeError

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/test', methods=['POST'])
def testModel():
	dados = request.get_json()
	X = dados.get('X')
	r = apiKayo(X)
	del X 
	gc.collect()
	#return json.dumps({'results': numpy.int64(r[0])}, default=convert)
	return str(r[0])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)