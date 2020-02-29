#!flask/bin/python
from flask import Flask, request
from apiKayo import apiKayo
from apiKayo import sendCloud
import gc
import os
import json
import numpy
from datetime import datetime
import threading

app = Flask(__name__)

def convert(o):
    if isinstance(o, numpy.int64): return int(o)  
    raise TypeError

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/test', methods=['POST'])
def testModel():
	# current date and time
	now = datetime.now()
	timestampINFog = datetime.timestamp(now)
	dados = request.get_json()
	dados['timestampINFog'] = timestampINFog
	X = dados.get('lista')
	print(dados)
	print(X)
	r = apiKayo(X)
	now = datetime.now()
	timestampOutFog = datetime.timestamp(now)
	dados['timestampOUTFog'] = timestampOutFog
	
	x = threading.Thread(target=sendCloud, args=(dados,))
	x.start()

	del X 
	gc.collect()
	#return json.dumps({'results': numpy.int64(r[0])}, default=convert)
	return str(r[0])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)






