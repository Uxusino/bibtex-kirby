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

    # Assuming that argument 'content' follows this dict structure:
    # {
    #   "label": (str),
    #   "data": (dict)
    #}
    def create_bibtex(self, content):
        #todo fiksaa nää
        current_time = datetime.now()

        sql = text(
            "INSERT INTO bibtex "
            "  (label, creation_time, modified_time, data) "
            "  VALUES (:label, :creation_time, :modified_time, :data)")
        insert = {
            "label": content['label'],
            "creation_time": current_time,
            "modified_time": current_time,
            "data": json.dumps(content['data'])
        }
        self._db.session.execute(sql, insert)
        self._db.session.commit()

bibtex_repository = BibtexRepository(db)