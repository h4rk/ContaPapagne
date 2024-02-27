
class CategoriaDto():
	id_categoria: int
	nome: str
	colore: str

	def __init__(self, id_categoria, nome, colore) -> None:
		self.id_categoria = id_categoria
		self.nome = nome
		self.colore = colore

	def __str__(self) -> str:
		return "CategoriaDto(id="+str(self.id_categoria)+", nome="+self.nome+", colore="+self.colore+")"
	
	
	def __repr__(self) -> str:
		return "CategoriaDto(id="+str(self.id_categoria)+", nome="+self.nome+", colore="+self.colore+")"