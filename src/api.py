import flask
from flask import render_template

import RPi.GPIO as GPIO  
import time

import sys
import os

sys.path.insert(0, os.getcwd()+"/robot")    
from Servo import Servo

name = 'hola'
servo_base = Servo("Base", 5)
servo_hombro = Servo("hombro", 3)
servo_codo = Servo("codo", 7)
servo_pinza = Servo("pinza", 8)
servo_base.rotate(5)
servo_hombro.rotate(70)
servo_codo.rotate(45)
servo_pinza.rotate(40)
time.sleep(1)
servo_pinza.rotate(85) # cerrado


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to the robot arm project</h1><p>This site is a prototype API for distant manage of a robot arm. <a href="/panel">panel</a></p>'

@app.route('/panel')
def panel():
    return render_template('panel.html',  name=name)

@app.route('/servo/<servoname>/<angle>')
def servo(servoname, angle):
	print servoname
	if (servoname == "base"):
		servo_base.rotate_step(angle)
	elif (servoname == "hombro"):
		servo_hombro.rotate_step(angle)
	elif (servoname == "codo"):
		servo_codo.rotate_step(angle)
	elif (servoname == "pinza"):
		if (angle == "5"):
			servo_pinza.rotate(40)
		else:
			servo_pinza.rotate(85)
	else:
		print "no servo"
	return 'Hello, World'

app.run(host='0.0.0.0')



