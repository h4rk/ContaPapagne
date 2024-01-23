from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, validates
from models.dbconfig import db

class CategoriaInvestimento(db.Model):
	__tablename__ = 'categoria_investimento'
	
	id_categoria_investimento = mapped_column(Integer, primary_key=True, autoincrement=True)
	nome = mapped_column(String)
	descrizione = mapped_column(String, nullable=True)

	def __str__(self):
		return 'Categoria(id='+ str(self.id_categoria_investimento) +', nome= '+ str(self.nome) +')'

	def __repr__(self):
		return 'Categoria(id='+ str(self.id_categoria_investimento) +', nome= '+ str(self.nome) +')'
