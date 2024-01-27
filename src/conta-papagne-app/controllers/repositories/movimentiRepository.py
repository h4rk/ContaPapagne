from models.dbconfig import db
from models.movimento_entrata import MovimentoEntrata
from sqlalchemy.sql import text
import datetime

def findById(id: int):
    db.create_all()
    db.session.add(MovimentoEntrata(2, datetime.date(2024, 1, 23), 123.45, None, None))
    db.session.commit()
    sql = text("SELECT * FROM movimento_entrata me WHERE me.id_entrata = :id")
    return db.session.execute(sql, {'id':id}).fetchone()