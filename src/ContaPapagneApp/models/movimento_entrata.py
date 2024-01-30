from datetime import date
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


	def __init__(self, data, importo, id_entrata=None, descrizione=None, risarcimento=None):
		self.data = data
		self.importo = importo
		self.descrizione = descrizione
		self.risarcimento = risarcimento
		if id_entrata is not None:
			self.id_entrata = id_entrata

	@staticmethod
	def build_from_dict(dict):
		try:
			id_entrata = dict.get('id_entrata', default=None)
			data = date.fromisoformat(dict.get('data_movimento'))
			importo = dict.get('importo_movimento')
			descrizione = dict.get('descrizione_movimento')
			risarcimento = dict.get('risarcimento')
			print('(id='+ str(id_entrata) +', importo= '+ str(importo) +', data='+str(data)+')')

			return MovimentoEntrata(data=data, importo=importo, id_entrata=id_entrata, descrizione=descrizione, risarcimento=risarcimento)
			
		except Exception as e:
			print("Impossibile generare l'oggetto a causa della seguente eccezione:")
			print(e)
	
	def __str__(self):
		return 'MovimentoEntrata(id='+ str(self.id_entrata) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'

	def __repr__(self):
		return 'MovimentoEntrata(id='+ str(self.id_entrata) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'
