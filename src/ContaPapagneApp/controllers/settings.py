from flask import Blueprint, render_template, request, current_app as app
from models.categoria import Categoria
from .repositories import categorieRepository as catRepo

set = Blueprint('settings', __name__, url_prefix='/settings')

@set.route('/', methods=['GET'])
def dashboard():
	return render_template('set/settings.html')

@set.route('/createCategoria',  methods=['POST'])
def createCategoria():
	cat = Categoria(nome=request.form.get('nome_categoria'), descrizione=request.form.get('descrizione_categoria'), tipologia=int(request.form.get('tipologia_categoria')))
	app.logger.info("Categoria da persistere: " + str(cat))
	result = catRepo.createCategoria(cat)
	return '';

@set.route('/listCategorie',  methods=['GET'])
def listCategorie():
	categorie = catRepo.listCategorie()
	app.logger.info("Categorie recuperate: \n" + str(categorie))
	return render_template('set/listaCategorie.html', categorie=categorie);