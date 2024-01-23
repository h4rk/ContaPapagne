from flask import Blueprint, render_template

bud = Blueprint('budgets', __name__, url_prefix='/budgets')

@bud.route('/', methods=['GET'])
def index():
	return render_template('budgets.html')