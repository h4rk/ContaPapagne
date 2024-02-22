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
	res = db.session.scalars(stmt).all()
	app.logger.debug("query result: \n" + str(res))

	return res

def findCategoriaWithNomeLike(hint):
	hint = f'%{hint}%'
	res = db.session.query(Categoria).filter(Categoria.nome.like(hint))
	app.logger.info("Result: " + str(res))

	return res
