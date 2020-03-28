import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the robot arm project</h1><p>This site is a prototype API for distant manage of a robot arm.</p>"

app.run()
