from models.dbconfig import db
from models.categoria_entrata import CategoriaEntrata
from models.categoria_uscita import CategoriaUscita

def createCategoriaEntrata(categoriaEntrata: CategoriaEntrata):
	db.session.add(categoriaEntrata)

def createCategoriaUscita(categoriaUscita: CategoriaUscita):
	db.session.add(categoriaUscita)
