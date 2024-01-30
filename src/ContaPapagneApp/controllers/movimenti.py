from flask import Blueprint, render_template, request
from models.movimento_entrata import MovimentoEntrata
from models.dbconfig import db

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
	movimenti = MovimentoEntrata.query.all()
	print(movimenti)
	return render_template('mov/lista-movimenti-short.html', movimenti=movimenti)

# Sezione API REST

@mov.route('/createMovimento', methods=['POST'])
def createMovimento():
	print('Request for createMovimenti(): ' + str(request.form))
	mov = MovimentoEntrata.build_from_dict(request.form)
	try:
		db.session.add(mov)
		db.session.commit()
	except Exception as e:
		return 'Errore scrittura DB' + str(e)
	
	# TODO: validazione campi
	#	
	# TODO: if insert OK return form con messaggio di OK
	#       else: return form con errore
	
	return render_template('mov/dashboard-movimenti.html')

@mov.route('/deleteMovimento', methods=['POST'])
def deleteMovimento():
	return render_template('common/insert-ok.html')