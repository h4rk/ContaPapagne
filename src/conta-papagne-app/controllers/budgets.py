from flask import Blueprint, render_template

bud = Blueprint('budgets', __name__, url_prefix='/budgets')

@bud.route('/', methods=['GET'])
def dashboard():
	return render_template('bud/budgets.html')