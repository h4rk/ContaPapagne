from dtos.categoria_dto import CategoriaDto
from dtos.movimento_dto import MovimentoDto
from models.categoria import Categoria
from models.categoria_movimento import CategoriaMovimento
from models.dbconfig import db, DBException
from models.movimento import Movimento
from sqlalchemy.sql import text, select

def findMovimentoById(id: int):
    sql = text("SELECT * FROM movimento m WHERE m.id_movimento = :id")
    return db.session.execute(sql, {'id':id}).fetchone()

def createMovimentoNC(mov: Movimento) -> Movimento:
    print(mov)
    db.session.add(mov)
    db.session.flush()
    return mov
    
def listMovimenti():
    try:
        sql = text(" SELECT * FROM movimento ORDER BY data DESC LIMIT 50")
        return db.session.execute(sql).fetchall()
    except Exception as e:
        print("Errore query listMovimenti")
        print(e)
        
def listMovimentiFull() -> list[MovimentoDto]:
    output = db.session.execute(select(Movimento.id_movimento, Movimento.data, Movimento.importo, Movimento.flag_entrata, Categoria.id_categoria, Categoria.nome, Categoria.colore)
                                .join(CategoriaMovimento, Movimento.id_movimento == CategoriaMovimento.id_movimento)
                                .join(Categoria, CategoriaMovimento.id_categoria == Categoria.id_categoria))

    movDtoList = []
    currentId = -1
    x = None
    for o in output:
        if currentId==-1:
            currentId = o[0]
            x = MovimentoDto(o[0], o[1], o[2], o[3], [])
            x.categorie.append(CategoriaDto(o[4], o[5], o[6]))
        elif currentId == o[0]:
            x.categorie.append(CategoriaDto(o[4], o[5], o[6]))
        else:
            movDtoList.append(x)
            currentId = o[0]
            x = MovimentoDto(o[0], o[1], o[2], o[3], [])
            x.categorie.append(CategoriaDto(o[4], o[5], o[6]))

    movDtoList.append(x)
    return movDtoList
