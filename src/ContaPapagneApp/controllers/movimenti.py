from flask import Blueprint, render_template, request

mov = Blueprint('movimenti', __name__, url_prefix='/movimenti')

@mov.route('/', methods=['GET'])
def dashboard():
	return render_template('mov/movimenti.html')

@mov.route('/createMovimento', methods=['POST'])
def createMovimento():
	print(request.get_data())
	return render_template('common/insert-ok.html')