from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "My Dogs"
    return render_template("fields.html", headline=headline)