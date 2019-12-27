from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world."

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}"

@app.route("/<string:name>")
def hello_first(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"    