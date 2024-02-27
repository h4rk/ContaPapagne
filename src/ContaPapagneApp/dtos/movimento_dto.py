import datetime
from dtos.categoria_dto import CategoriaDto

class MovimentoDto():
	id_movimento: int
	importo: float
	data: datetime.date
	flag_entrata: bool
	categorie: list[CategoriaDto]

	def __init__(self, id, data,importo, flag_entrata, categorie) -> None:
		self.id = id
		self.importo = importo
		self.data = data
		self.flag_entrata = flag_entrata
		self.categorie = categorie

	def __str__(self) -> str:
		return "MovimentoDto(id="+str(self.id)+", importo="+str(self.importo)+", data="+str(self.data)+")"
	
	
	def __repr__(self) -> str:
		return "MovimentoDto(id="+str(self.id)+", importo="+str(self.importo)+", data="+str(self.data)+")"