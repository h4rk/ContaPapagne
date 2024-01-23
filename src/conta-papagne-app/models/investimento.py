from sqlalchemy import Integer, String, Date, Double, ForeignKey
from sqlalchemy.orm import mapped_column
from models.dbconfig import db

class Investimento(db.Model):
	__tablename__ = 'investimento'
	
	id_investimento = mapped_column(Integer, primary_key=True, autoincrement=True)
	data_inizio = mapped_column(Date)
	data_fine = mapped_column(Date)
	importo_nominale = mapped_column(Double)
	categoria = mapped_column(ForeignKey('categoria_investimento.id_categoria_investimento'))
	descrizione = mapped_column(String, nullable=True)

	def __str__(self):
		return 'Investimento(id='+ str(self.id_investimento) +', importo_nominale= '+ str(self.importo_nominale) +', data_inizio='+str(self.data_inizio)+')'

	def __repr__(self):
		return 'Investimento(id='+ str(self.id_investimento) +', importo_nominale= '+ str(self.importo_nominale) +', data_inizio='+str(self.data_inizio)+')'
