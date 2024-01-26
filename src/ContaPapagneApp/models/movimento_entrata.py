from sqlalchemy import Integer, String, Date, Double, ForeignKey
from sqlalchemy.orm import mapped_column
from models.dbconfig import db

class MovimentoEntrata(db.Model):
	__tablename__ = 'movimento_entrata'
	
	id_entrata = mapped_column(Integer, primary_key=True, autoincrement=True)
	data = mapped_column(Date)
	importo = mapped_column(Double)
	descrizione = mapped_column(String, nullable=True)
	risarcimento = mapped_column(ForeignKey('movimento_uscita.id_uscita'), nullable=True)

	def __str__(self):
		return 'MovimentoEntrata(id='+ str(self.id_entrata) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'

	def __repr__(self):
		return 'MovimentoEntrata(id='+ str(self.id_entrata) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'
