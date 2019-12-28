from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        name = request.args.get("name")
        return render_template("hello.html", name=name)
    else:    
        name = request.form.get("name")
        return render_template("hello.html", name=name)

@app.route("/note", methods=["GET", "POST"])
def note():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":   
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("note.html", notes=session["notes"])
