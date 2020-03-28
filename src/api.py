import flask
from flask import render_template

import RPi.GPIO as GPIO  
import time

import sys
import os
#sys.path.insert(0, "/home/pi/Desktop/robotarm/src/robot")
sys.path.insert(0, os.getcwd()+"/robot")    
from Servo import Servo

name = 'hola'
servo_base = Servo("Base", 5)
servo_base.rotate(5)

app = flask.Flask(__name__)
app.config["DEBUG"] = True
#app.run(host='0.0.0.0')


@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to the robot arm project</h1><p>This site is a prototype API for distant manage of a robot arm. <a href="/panel">panel</a></p>'

@app.route('/panel')
def panel():
    return render_template('panel.html',  name=name)

@app.route('/servo/<servoname>/<angle>')
def servo(servoname, angle):
	servo_base.rotate_step()
	return 'Hello, World'

app.run(host='0.0.0.0')



