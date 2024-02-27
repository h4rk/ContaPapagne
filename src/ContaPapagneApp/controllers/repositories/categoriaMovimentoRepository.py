from models.dbconfig import db
from models.categoria import Categoria
from models.categoria_movimento import CategoriaMovimento

def createCategorieMovimentoNC(id_movimento: int, lista_categorie: list[Categoria]):
    for cat in lista_categorie:
        db.session.add(CategoriaMovimento(cat.id_categoria, id_movimento))
    db.session.flush()
