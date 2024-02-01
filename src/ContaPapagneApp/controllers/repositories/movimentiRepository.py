from models.dbconfig import db
from models.movimento_entrata import MovimentoEntrata
from models.movimento_uscita import MovimentoUscita
from sqlalchemy.sql import text
import datetime

def findEntrataById(id: int):
    # db.create_all()
    # db.session.add(MovimentoEntrata(2, datetime.date(2024, 1, 23), 123.45, None, None))
    # db.session.commit()
    sql = text("SELECT * FROM movimento_entrata me WHERE me.id_entrata = :id")
    return db.session.execute(sql, {'id':id}).fetchone()

def findUscitaById(id: int):
    # db.create_all()
    # db.session.add(MovimentoUscita(2, datetime.date(2024, 1, 23), 123.45, None, None))
    # db.session.commit()
    sql = text("SELECT * FROM movimento_uscita mu WHERE mu.id_uscita = :id")
    return db.session.execute(sql, {'id':id}).fetchone()

def createEntrata(movEntrata) -> bool:
    try:
        db.session.add(movEntrata)
        db.session.commit()
        return True
    except Exception as e:
        print('Errore scrittura DB' + str(e))
        return False

def listMovimenti():
    try:
        sql = text(""" SELECT * FROM (SELECT mu.data, mu.importo, mu.descrizione FROM movimento_uscita mu UNION ALL SELECT me.data, me.importo, me.descrizione FROM movimento_entrata me) dum ORDER BY data DESC LIMIT 50""")
        return db.session.execute(sql).fetchall()
    except Exception as e:
        print("Errore query listMovimenti")
        print(e)
