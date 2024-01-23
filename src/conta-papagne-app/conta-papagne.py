from flask import Flask, render_template
from controllers.movimenti import mov
from controllers.investimenti import inv
from controllers.budgets import bud
from controllers.settings import set
from models.dbconfig import db

#Create app
app = Flask(__name__)

#Setup DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

#Register blueprints
app.register_blueprint(mov)
app.register_blueprint(inv)
app.register_blueprint(bud)
app.register_blueprint(set)

@app.route("/")
def home():
    return render_template("dashboard-variant.html")
