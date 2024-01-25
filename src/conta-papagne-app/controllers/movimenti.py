from flask import Blueprint, render_template

mov = Blueprint('movimenti', __name__, url_prefix='/movimenti')

@mov.route('/', methods=['GET'])
def dashboard():
	return render_template('mov/movimenti.html')