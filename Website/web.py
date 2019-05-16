import config
from flask import Flask, render_template, redirect, request, jsonify
import time
import sys
import logging


app = Flask(__name__)

# Disable request logging in terminal(doesn't matter in cpu usage that much for rpi 3b+)

# log = logging.getLogger('werkzeug')
# log.disabled = True



jsondata = {}
adata = {}


@app.route('/')
@app.route('/index')
def hello():
	
	return render_template('index.html', page='home')

@app.route("/led")
def LED():	
	return render_template('index.html', 
		functdict=config.functdict, 
		color_rgb=config.color_rgb, 
		length=config.length,
		wait=config.wait,
		page='led')

@app.route("/led/<string:functions>")
def functions(functions):
	config.function = str(functions)
	return redirect('/led', code=302)
	
@app.route("/led/<string:color>/<int:value>")
def colorcontrol(color, value):
	config.color_rgb[color] = int(value)
	return redirect('/led', code=302)
	

@app.route("/led/length/<int:value>")
def length(value):
	config.length = value
	return redirect('/led', code=302)

@app.route("/led/wait/<float:value>")
def wait(value):
	config.wait = value
	return redirect('/led', code=302)

@app.route("/led/brightness/<float:value>")
def brightness(value):
	config.brightness = value
	return ('', 204)


@app.route("/led/data")
def data():
	global jsondata
	try:
		jsondata['color'] = config.color_rgb
		jsondata['temp'] = config.temperature
		jsondata['wait'] = config.wait
		jsondata['cpu_load'] = config.cpu_load
	except:
		for i in jsondata:
			jsondata[i] = 0
		
	return jsonify(jsondata), 200

@app.route("/led/arduino/<int:value>")
def arduino(value):
	global adata
	adata['led'] = config.color_rgb['b']
	return redirect('/led', code=302)
	
	
@app.route("/arduinodata")
def arduinodata():
	global adata
	adata = config.color_rgb_arduino
	adata['wait'] = config.wait
	return jsonify(adata), 200

@app.route("/color", methods=["POST"])
def JSONcolor():
	config.color_rgb = request.get_json(force=True)
	return ('', 204)
