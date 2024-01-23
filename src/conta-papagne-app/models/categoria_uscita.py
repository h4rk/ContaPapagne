from sqlalchemy import ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import mapped_column
from models.dbconfig import db

class CategoriaUscita(db.Model):
	__tablename__ = 'categoria_uscita'
	
	id_categoria = mapped_column(ForeignKey('categoria.id_categoria'), nullable=False)
	id_uscita = mapped_column(ForeignKey('movimento_uscita.id_uscita'), nullable=False)
	__table_args__ = (
		UniqueConstraint('id_categoria', 'id_uscita', name='id_cat_id_usc_unique'),
		PrimaryKeyConstraint('id_categoria', 'id_uscita', name='categoria_uscita_pk')
		)