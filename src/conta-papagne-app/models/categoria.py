from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, validates
from models.dbconfig import db

class Categoria(db.Model):
	__tablename__ = 'categoria'
	
	id_categoria = mapped_column(Integer, primary_key=True, autoincrement=True)
	nome = mapped_column(String)
	tipologia = mapped_column(Integer,)
	descrizione = mapped_column(String, nullable=True)

	#Validatore automatico per il campo tipologia, che rappresenta la tipologia di categoria, ovvero:
	# 0 = categoria per soli movimenti in entrata
	# 1 = categoria per soli movimenti in uscita
	# 2 = categoria per entrambi movimenti in entrata e uscita
	@validates('tipologia')
	def validate_tipologia(self, key, tipologia):
		if not 0 <= tipologia <= 2:
			raise ValueError('Il valore "tipologia" per la tabella "Categoria" deve essere uno tra [0, 1, 2].')
		else:
			return tipologia

	def __str__(self):
		return 'Categoria(id='+ str(self.id_categoria) +', nome= '+ str(self.nome) +', tipologia='+str(self.tipologia)+')'

	def __repr__(self):
		return 'Categoria(id='+ str(self.id_categoria) +', nome= '+ str(self.nome) +', tipologia='+str(self.tipologia)+')'
