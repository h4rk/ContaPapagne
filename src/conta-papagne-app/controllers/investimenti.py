from flask import Blueprint, render_template

inv = Blueprint('investimenti', __name__, url_prefix='/investimenti')

@inv.route('/', methods=['GET'])
def dashboard():
	return render_template('inv/investimenti.html')