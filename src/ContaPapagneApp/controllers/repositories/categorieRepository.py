from models.dbconfig import db
from sqlalchemy import select
from models.categoria import Categoria

def createCategoria(categoria: Categoria) -> int:
	db.session.add(categoria)	
	db.session.commit()
	return categoria.id_categoria

def listCategorie():
	stmt = select(Categoria)
	print(stmt)
	res = db.session.scalars(stmt).all()
	for r in res:
		print(r)
	return res

