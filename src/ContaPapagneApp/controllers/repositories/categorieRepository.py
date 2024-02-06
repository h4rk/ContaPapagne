from models.dbconfig import db
from sqlalchemy import select, text
from models.categoria import Categoria
from flask import current_app as app

def createCategoria(categoria: Categoria) -> int:
	db.session.add(categoria)
	db.session.commit()
	return categoria.id_categoria

def listCategorie():
	stmt = select(Categoria)
	app.logger.debug("listCategorie query: \n" + str(stmt))
	res = db.session.scalars(stmt).all()
	return res

def findCategoriaWithNomeLike(hint):
	hint = f'%{hint}%'
	stmt =text("SELECT * FROM categoria c WHERE c.nome LIKE :hint")
	res = db.session.execute(stmt, {'hint': hint}).all()
	return res
