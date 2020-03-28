import flask
from flask import render_template

name = 'hola'

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the robot arm project</h1><p>This site is a prototype API for distant manage of a robot arm.</p>"

@app.route('/panel')
def panel():
    return render_template('panel.html',  name=name)

@app.route('/servo/<servoname>/<int:anlge>')
def servo(servoname, angle):
    return 'Hello, World'

app.run()



