from datetime import date
from sqlalchemy import Integer, String, Date, Double, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column
from models.dbconfig import db

class Movimento(db.Model):
	__tablename__ = 'movimento'
	
	id_movimento = mapped_column(Integer, primary_key=True, autoincrement=True)
	data = mapped_column(Date)
	importo = mapped_column(Double)
	flag_entrata = mapped_column(Boolean)
	descrizione = mapped_column(String, nullable=True)
	risarcimento = mapped_column(ForeignKey('movimento.id_movimento'), nullable=True)

	def __init__(self, data, importo, flag_entrata, id_movimento=None, descrizione=None, risarcimento=None):
		self.data = data
		self.importo = importo
		self.flag_entrata = flag_entrata
		self.descrizione = descrizione
		self.risarcimento = risarcimento
		if id_movimento is not None:
			self.id_movimento = id_movimento

	@staticmethod
	def build_from_dict(dict):
		try:
			id_movimento = dict.get('id_entrata', default=None)
			data = date.fromisoformat(dict.get('data_movimento'))
			importo = dict.get('importo_movimento')
			if dict.get('flag_entrata') == 'true':
				flag_entrata = True
			else:
				flag_entrata = False
			descrizione = dict.get('descrizione_movimento')
			risarcimento = dict.get('risarcimento')

			return Movimento(data=data, importo=importo,flag_entrata=flag_entrata, id_movimento=id_movimento, descrizione=descrizione, risarcimento=risarcimento)
			
		except Exception as e:
			print("Impossibile generare l'oggetto a causa della seguente eccezione:\n")
			print(e)
	
	def __str__(self):
		return 'Movimento(id='+ str(self.id_movimento) +', importo='+ str(self.importo) +', data='+str(self.data) +', flag_entrata='+ str(self.flag_entrata) +', risarcimento='+ str(self.risarcimento)+')'

	def __repr__(self):
		return 'Movimento(id='+ str(self.id_movimento) +', importo='+ str(self.importo) +', data='+str(self.data) +', flag_entrata='+ str(self.flag_entrata) +', risarcimento='+ str(self.risarcimento)+')'
