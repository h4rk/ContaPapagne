from models.dbconfig import db
from models.categoria_movimento import CategoriaMovimento

def createCategoriaMovimento(id_movimento: int, lista_id_categorie: list[CategoriaMovimento]):
    for id in lista_id_categorie:
        db.session.add(CategoriaMovimento(id, id_movimento))
    db.session.flush()
