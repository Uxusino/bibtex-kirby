from config import db
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

from entities.bibtex import Bibtex

class BibtexRepository:
    def __init__(self, database: SQLAlchemy):
        self._db = database

    # Returns list of Bibtex instances
    def get_bibtexs(self) -> list[Bibtex]:
        #todo fiksaa nää
        result = self._db.session.execute(text("SELECT * FROM bibtex"))
        bibtexs = result.fetchall()
        bibs = []
        for b in bibtexs:
            bibs.append(Bibtex(b))
        return bibs
    
    def get_bibtex_by_label(self, label: str) -> Bibtex:
        sql = text("SELECT * FROM bibtex WHERE label = (:label)")
        result = self._db.session.execute(sql, {"label": label})
        bibtex = result.fetchone()
        bib = Bibtex(bibtex)
        return bib

    # Assuming that argument 'content' follows this dict structure:
    # {
    #   "label": (str),
    #   "type": (str),
    #   "data": (dict)
    #}
    def create_bibtex(self, content):
        #todo fiksaa nää
        current_time = datetime.now()

        sql = text(
            "INSERT INTO bibtex "
            "  (label, type, creation_time, modified_time, data) "
            "  VALUES (:label, :type, :creation_time, :modified_time, :data)")
        insert = {
            "label": content['label'],
            "type": content['type'],
            "creation_time": current_time,
            "modified_time": current_time,
            "data": json.dumps(content['data'])
        }
        self._db.session.execute(sql, insert)
        self._db.session.commit()

    def reset_db(self):
        sql = text(f"DELETE FROM bibtex")
        self._db.session.execute(sql)
        self._db.session.commit()

    def delete_bibtex(self, id: int):
        sql = text("DELETE FROM bibtex WHERE id = :id")
        self._db.session.execute(sql, {"id": id})
        self._db.session.commit()

bibtex_repository = BibtexRepository(db)