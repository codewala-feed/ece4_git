from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "You are in homepage"

@app.route("/new-feature", methods=["POST"])
def feature():
    return "New Feature Added"