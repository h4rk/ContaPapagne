from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard-variant.html")

@app.route("/categorie")
def categorie():
    return render_template("categorie.html")

@app.route("/movimenti")
def movimenti():
    return render_template("movimenti.html")

@app.route("/investimenti")
def investimenti():
    return render_template("investimenti.html")