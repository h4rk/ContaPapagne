from sqlalchemy import Integer, String, Date, Double
from sqlalchemy.orm import mapped_column
from models.dbconfig import db

class MovimentoUscita(db.Model):
	__tablename__ = 'movimento_uscita'
	
	id_uscita = mapped_column(Integer, primary_key=True, autoincrement=True)
	data = mapped_column(Date)
	importo = mapped_column(Double)
	descrizione = mapped_column(String, nullable=True)

	def __str__(self):
		return 'MovimentoUscita(id='+ str(self.id_uscita) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'

	def __repr__(self):
		return 'MovimentoUscita(id='+ str(self.id_uscita) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'
