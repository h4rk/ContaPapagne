from flask import Blueprint, render_template, request, current_app as app
from models.categoria_entrata import CategoriaEntrata
from models.movimento_entrata import MovimentoEntrata
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
	mov = MovimentoEntrata.build_from_dict(request.form)
	# TODO: validazione campi ? 
	try:
		createMovEntrataHelper(mov, request.form.get('id_categoria'))
		return render_template('mov/dashboard-movimenti.html')
	except Exception as e:
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

def createMovEntrataHelper(movimentoEntrata, id_categoria):
		movEnt = movRepo.createEntrata(movimentoEntrata)
		catMovEnt = CategoriaEntrata(id_categoria, movEnt.id_entrata)
		catMovRepo.createCategoriaEntrata(catMovEnt)

def listMovimentiHelper():
	movRepo.listMovimenti()