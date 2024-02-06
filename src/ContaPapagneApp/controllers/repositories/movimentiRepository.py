from models.dbconfig import db
from models.movimento_entrata import MovimentoEntrata
from models.movimento_uscita import MovimentoUscita
from sqlalchemy.sql import text
from flask import current_app as app

def findEntrataById(id: int):
    sql = text("SELECT * FROM movimento_entrata me WHERE me.id_entrata = :id")
    return db.session.execute(sql, {'id':id}).fetchone()

def findUscitaById(id: int):
    sql = text("SELECT * FROM movimento_uscita mu WHERE mu.id_uscita = :id")
    return db.session.execute(sql, {'id':id}).fetchone()

def createEntrata(movEntrata) -> int:
    try:
        db.session.add(movEntrata)
        db.session.commit()
        return movEntrata.id_entrata
    except Exception as e:
        app.logger.error('Errore scrittura DB\n' + str(e))
        return -1

def listMovimenti():
    try:
        sql = text(""" SELECT * FROM (SELECT mu.data, mu.importo, mu.descrizione FROM movimento_uscita mu UNION ALL SELECT me.data, me.importo, me.descrizione FROM movimento_entrata me) dum ORDER BY data DESC LIMIT 50""")
        return db.session.execute(sql).fetchall()
    except Exception as e:
        print("Errore query listMovimenti")
        print(e)
