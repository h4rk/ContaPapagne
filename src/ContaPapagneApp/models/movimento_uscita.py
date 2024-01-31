from datetime import date
from sqlalchemy import Integer, String, Date, Double
from sqlalchemy.orm import mapped_column
from models.dbconfig import db

class MovimentoUscita(db.Model):
	__tablename__ = 'movimento_uscita'
	
	id_uscita = mapped_column(Integer, primary_key=True, autoincrement=True)
	data = mapped_column(Date)
	importo = mapped_column(Double)
	descrizione = mapped_column(String, nullable=True)

	def __init__(self, data, importo, id_uscita=None, descrizione=None):
		self.data = data
		self.importo = importo
		self.descrizione = descrizione
		if id_uscita is not None:
			self.id_uscita = id_uscita

	@staticmethod
	def build_from_dict(dict):
		try:
			id_uscita = dict.get('id_uscita', default=None)
			data = date.fromisoformat(dict.get('data_movimento'))
			importo = dict.get('importo_movimento')
			descrizione = dict.get('descrizione_movimento')

			return MovimentoUscita(data=data, importo=importo, id_uscita=id_uscita, descrizione=descrizione)
			
		except Exception as e:
			print("Impossibile generare l'oggetto a causa della seguente eccezione:\n")
			print(e)

	def __str__(self):
		return 'MovimentoUscita(id='+ str(self.id_uscita) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'

	def __repr__(self):
		return 'MovimentoUscita(id='+ str(self.id_uscita) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'
