from flask import Blueprint, render_template, request, current_app as app
from models.movimento_entrata import MovimentoEntrata
from models.dbconfig import db
from .repositories import movimentiRepository as movRepo, categorieRepository as catRepo
import time

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
	time.sleep(2)
	movimenti = movRepo.listMovimenti()
	print(movimenti)
	return render_template('mov/lista-movimenti.html', movimenti=movimenti)


@mov.route('/createMovimento', methods=['POST'])
def createMovimento():
	print('Request for createMovimenti(): ' + str(request.form))
	mov = MovimentoEntrata.build_from_dict(request.form)
	
	# TODO: validazione campi
	
	esito = movRepo.createEntrata(mov)
	if esito<0:
		# TODO errore
		return render_template('mov/dashboard-movimenti.html')
	else:
		return render_template('mov/dashboard-movimenti.html')

#TODO: aggiungere parametro id da cancellare, cancellazione
@mov.route('/deleteMovimento', methods=['DELETE'])
def deleteMovimento():
	return render_template('mov/lista-movimenti.html')

#TODO
@mov.route('/putMovimento', methods=['PUT'])
def putMovimento():
	return render_template('mov/dettaglio-movimento.html')

@mov.route('/fetchCategorie', methods=['GET'])
def fetchCategorie():
	if (request.args.get('categoria_movimento') != ''):
		categorie = catRepo.findCategoriaWithNomeLike(request.args.get('categoria_movimento'))
	else:
		categorie = []
	app.logger.debug(categorie)
	return render_template('mov/list-categorie.html', categorie=categorie)
