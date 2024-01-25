from flask import Flask, render_template
from controllers.movimenti import mov
from controllers.investimenti import inv
from controllers.budgets import bud
from controllers.settings import set
from models.dbconfig import db
from models.movimento_uscita import MovimentoUscita
from models.movimento_entrata import MovimentoEntrata
import datetime

#Create app
app = Flask(__name__)

#Setup DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
""" with app.app_context():
    db.create_all()
    db.session.add(MovimentoEntrata(data=datetime.date(2024, 1, 23), importo=123.45, descrizione=None, risarcimento=None))
    db.session.commit()
    for q in db.session.execute(db.select(MovimentoEntrata)):
        print(q) """

#Register blueprints
app.register_blueprint(mov)
app.register_blueprint(inv)
app.register_blueprint(bud)
app.register_blueprint(set)

@app.route("/")
def home():
    return render_template("index.html")
