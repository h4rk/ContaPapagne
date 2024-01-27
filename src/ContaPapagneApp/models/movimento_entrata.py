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

	@classmethod
	def build_from_dict(self, dict):
		try:
			if dict.id_entrata is not None:
				self.id_entrata = dict.id_entrata
			self.data = dict.data
			self.importo = dict.importo
			self.descrizione = dict.descrizione
			self.risarcimento = dict.risarcimento

			return self
		except Exception as e:
			print("Impossibile generare l'oggetto a causa della seguente eccezione:")
			print(e)
	
	def __str__(self):
		return 'MovimentoEntrata(id='+ str(self.id_entrata) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'

	def __repr__(self):
		return 'MovimentoEntrata(id='+ str(self.id_entrata) +', importo= '+ str(self.importo) +', data='+str(self.data)+')'
