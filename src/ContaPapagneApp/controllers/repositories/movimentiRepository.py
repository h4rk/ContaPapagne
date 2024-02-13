from models.dbconfig import db, DBException
from models.movimento import Movimento
from sqlalchemy.sql import text

def findMovimentoById(id: int):
    sql = text("SELECT * FROM movimento m WHERE m.id_movimento = :id")
    return db.session.execute(sql, {'id':id}).fetchone()

def createMovimento(mov) -> Movimento:
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
