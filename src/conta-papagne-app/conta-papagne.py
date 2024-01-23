from flask import Flask, render_template
from blueprints.movimenti import mov
from blueprints.investimenti import inv
from blueprints.budgets import bud
from blueprints.settings import set
app = Flask(__name__)
app.register_blueprint(mov)
app.register_blueprint(inv)
app.register_blueprint(bud)
app.register_blueprint(set)

@app.route("/")
def home():
    return render_template("dashboard-variant.html")
