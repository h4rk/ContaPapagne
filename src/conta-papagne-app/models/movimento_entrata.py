from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from dbconfig import db

class MovimentoEntrata(db.Model):
	idMovimento: Mapped[int] = mapped_column(primary_key=True)
	