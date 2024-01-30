from flask import Blueprint, render_template, request

mov = Blueprint('movimenti', __name__, url_prefix='/movimenti')

# Sezione endpoint HTMX

@mov.route('/', methods=['GET'])
def dashboard():
	return render_template('mov/dashboard-movimenti.html')

@mov.route('/dettaglioMovimento', methods=['GET'])
def dettaglioMovimento():
	return render_template('mov/dettaglio-movimento.html')

@mov.route('/listaMovimenti', methods=['GET'])
def listaMovimenti():
	return render_template('mov/lista-movimenti.html')

# Sezione API REST

@mov.route('/createMovimento', methods=['POST'])
def createMovimento():
	print('Request for createMovimenti(): ' + str(request.get_data()))
	return render_template('common/insert-ok.html')

@mov.route('/deleteMovimento', methods=['POST'])
def deleteMovimento():
	return render_template('common/insert-ok.html')