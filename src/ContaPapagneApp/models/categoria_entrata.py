from sqlalchemy import ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import mapped_column, validates
from models.dbconfig import db

class CategoriaEntrata(db.Model):
	__tablename__ = 'categoria_entrata'
	
	id_categoria = mapped_column(ForeignKey('categoria.id_categoria'), nullable=False)
	id_entrata = mapped_column(ForeignKey('movimento_entrata.id_entrata'), nullable=False)
	__table_args__ = (
		UniqueConstraint('id_categoria', 'id_entrata', name='id_cat_id_ent_unique'),
		PrimaryKeyConstraint('id_categoria', 'id_entrata', name='categoria_entrata_pk')
		)