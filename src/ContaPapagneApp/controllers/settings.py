from flask import Blueprint, render_template, request
from models.categoria import Categoria
from .repositories import categorieRepository as catRepo

set = Blueprint('settings', __name__, url_prefix='/settings')

@set.route('/', methods=['GET'])
def dashboard():
	return render_template('set/settings.html')

@set.route('/createCategoria',  methods=['POST'])
def createCategoria():
	cat = Categoria(nome=request.form.get('nome_categoria'), descrizione=request.form.get('descrizione_categoria'), tipologia=int(request.form.get('tipologia_categoria')))
	result = catRepo.createCategoria(cat)
	return '';

@set.route('/listCategorie',  methods=['GET'])
def listCategorie():
	categorie = catRepo.listCategorie()
	print(categorie)
	return render_template('set/listaCategorie.html', categorie=categorie);