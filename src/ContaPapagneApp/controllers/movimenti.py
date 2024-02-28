from flask import Blueprint, render_template, request, current_app as app
from models.movimento import Movimento
from models.categoria import Categoria
from models.dbconfig import db
from .repositories import movimentiRepository as movRepo, categorieRepository as catRepo, categoriaMovimentoRepository as catMovRepo
from dtos.movimento_dto import MovimentoDto	

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
	movimenti:list[MovimentoDto] = movRepo.listMovimentiFull()
	return render_template('mov/lista-movimenti.html', movimenti=movimenti)


@mov.route('/createMovimento', methods=['POST'])
def createMovimento():
	mov : Movimento = Movimento.build_from_dict(request.form)
	mov : Movimento = movRepo.createMovimentoNC(mov)
	categorieList: list[Categoria] = catRepo.listNcategorie(request.form.getlist('categorie_movimento'))
	catMovRepo.createCategorieMovimentoNC(mov.id_movimento, categorieList)
	db.session.commit()

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
	if (request.args.get('multiRicerca') != ''):
		categorie = catRepo.findCategoriaWithNomeLikeAndTipoMovimento(request.args.get('multiRicerca'), request.args.get('tipo_movimento'))
		app.logger.debug(categorie)
	else:
		categorie=[]
	return render_template('mov/list-categorie.html', categorie=categorie)
