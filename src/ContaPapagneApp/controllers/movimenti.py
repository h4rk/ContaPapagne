from flask import Blueprint, render_template, request
from models.movimento_entrata import MovimentoEntrata
from models.dbconfig import db
import time

mov = Blueprint('movimenti', __name__, url_prefix='/movimenti')

# Sezione endpoint HTMX

@mov.route('/', methods=['GET'])
def dashboard():
	return render_template('mov/dashboard-movimenti.html')

@mov.route('/dettaglioMovimento', methods=['GET'])
def dettaglioMovimento():
	return render_template('mov/dettaglio-movimento.html')

#TODO
@mov.route('/putMovimento', methods=['PUT'])
def putMovimento():
	return render_template('mov/dettaglio-movimento.html')

@mov.route('/listaBreveMovimenti', methods=['GET'])
def listaBreveMovimenti():
	time.sleep(2)
	movimenti = db.session.execute(db.select(MovimentoEntrata).order_by(MovimentoEntrata.data)).fetchmany(5)
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

#TODO: aggiungere parametro id da cancellare, cancellazione
@mov.route('/deleteMovimento', methods=['DELETE'])
def deleteMovimento():
	return render_template('mov/lista-movimenti.html')