from flask import Blueprint, render_template

inv = Blueprint('investimenti', __name__, url_prefix='/investimenti')

@inv.route('/', methods=['GET'])
def index():
	return render_template('investimenti.html')