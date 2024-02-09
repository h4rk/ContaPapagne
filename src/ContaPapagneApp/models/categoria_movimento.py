from sqlalchemy import ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import mapped_column
from models.dbconfig import db

class CategoriaMovimento(db.Model):
	__tablename__ = 'categoria_movimento'
	
	id_categoria = mapped_column(ForeignKey('categoria.id_categoria'), nullable=False)
	id_movimento = mapped_column(ForeignKey('movimento.id_movimento'), nullable=False)
	__table_args__ = (
		UniqueConstraint('id_categoria', 'id_movimento', name='id_cat_id_mov_unique'),
		PrimaryKeyConstraint('id_categoria', 'id_movimento', name='categoria_movimento_pk')
		)
	
	def __init__(self, id_categoria, id_movimento) -> None:
		self.id_categoria = id_categoria
		self.id_movimento = id_movimento