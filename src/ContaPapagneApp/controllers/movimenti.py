from flask import Blueprint, render_template, request, current_app as app
from models.movimento import Movimento
from models.dbconfig import db
from .repositories import movimentiRepository as movRepo, categorieRepository as catRepo, categoriaMovimentoRepository as catMovRepo
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
	movimenti = movRepo.listMovimenti()
	return render_template('mov/lista-movimenti.html', movimenti=movimenti)


@mov.route('/createMovimento', methods=['POST'])
def createMovimento():
	mov = Movimento.build_from_dict(request.form)
	mov = movRepo.createMovimento(mov)
	#
	#catMovRepo.createCategoriaMovimento(mov.id_movimento, )
	print(mov)
	# TODO: validazione campi ? 
	# TODO implementazione
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
	output = []
	if (request.args.get('categoria_movimento') != ''):
		categorie = catRepo.findCategoriaWithNomeLike(request.args.get('categoria_movimento'))
		for cat in categorie:
			output.append(cat.toDict())
		app.logger.debug(output)

	return output