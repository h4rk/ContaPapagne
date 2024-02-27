from models.dbconfig import db
from sqlalchemy import select, and_
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

def findCategoriaWithNomeLikeAndTipoMovimento(hint:str, tipologia:str):
	hint = f'%{hint}%'
	excluded = 1 if tipologia=="true" else 0
	print('-----: Excluded: ' + str(excluded))
	stmt = select(Categoria).where(and_(Categoria.nome.like(hint),Categoria.tipologia != excluded))
	res = db.session.execute(stmt).scalars()
	app.logger.info("-----: Result: " + str(res))

	return res

def listNcategorie(l: list[int]) -> list[Categoria]:
	r: list[Categoria] = []
	for id in l:
		r.append(db.session.query(Categoria).filter(Categoria.id_categoria == id).one())
	print(r)
	return r