from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    dognames = ["Samoyed", "Huskey", "Akita Inu", "Corgi", "Chau-chau"]
    return render_template("fields.html", dognames=dognames)