import json
from datetime import datetime

from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

from config import db
from entities.bibtex import Bibtex

class BibtexRepository:
    def __init__(self, database: SQLAlchemy):
        self._db = database

    # Returns list of Bibtex instances
    def get_bibtexs(self) -> list[Bibtex]:
        result = self._db.session.execute(text("SELECT * FROM bibtex"))
        bibtexs = result.fetchall()
        bibs = []
        for b in bibtexs:
            new_bibtex = Bibtex(b)
            tags = self._get_tags_by_id(new_bibtex.id)
            if len(tags) != 0:
                new_bibtex.set_tags(tags)
            bibs.append(new_bibtex)
        return bibs

    def get_bibtex_by_label(self, label: str) -> Bibtex:
        sql = text("SELECT * FROM bibtex WHERE label = (:label)")
        result = self._db.session.execute(sql, {"label": label})
        bibtex = result.fetchone()
        bib = Bibtex(bibtex)
        tags = self._get_tags_by_id(bib.id)
        if len(tags) != 0:
            bib.set_tags(tags)
        return bib

    # Assuming that argument 'content' follows this dict structure:
    # {
    #   "label": (str),
    #   "type": (str),
    #   "data": (dict),
    #   "tags": (list[str])
    #}
    # Returns id
    def create_bibtex(self, content) -> str:
        current_time = datetime.now()
        label = content['label']

        sql = text(
            "INSERT INTO bibtex "
            "  (label, type, creation_time, modified_time, data) "
            "  VALUES (:label, :type, :creation_time, :modified_time, :data) "
            "RETURNING id")
        insert = {
            "label": label,
            "type": content['type'],
            "creation_time": current_time,
            "modified_time": current_time,
            "data": json.dumps(content['data'])
        }
        result = self._db.session.execute(sql, insert)
        bibtex_id = result.fetchone()[0]

        self._db.session.commit()
        
        return bibtex_id

    def update_bibtex(self, ref_id: int, content: dict[str | dict]):
        current_time = datetime.now()

        sql = text(
            "UPDATE bibtex "
            "  SET "
            "  label = :label, "
            "  modified_time = :modified_time, "
            "  data = :data "
            "  WHERE id = :id "
        )
        update = {
            "label": content['label'],
            "modified_time": current_time,
            "data": json.dumps(content['data']),
            "id": ref_id
        }
        self._db.session.execute(sql, update)
        self._db.session.commit()

    def add_tag(self, bib_id: int, tag: str):
        sql = text(
            "INSERT INTO tags "
            "  (name, bibtex_id) "
            "  VALUES (:name, :bibtex_id)"
        )
        insert = {
            "name": tag,
            "bibtex_id": bib_id
        }
        self._db.session.execute(sql, insert)
        self._db.session.commit()

    def _get_tags_by_id(self, bib_id: int) -> list[str]:
        sql = text(
            "SELECT name FROM tags WHERE bibtex_id = (:bibtex_id)"
        )
        bibtex_id = {"bibtex_id": bib_id}
        result = self._db.session.execute(sql, bibtex_id).fetchall()
        tags = [tag[0] for tag in result]
        return tags

    def reset_db(self):
        tables = ["bibtex", "tags"]
        for table in tables:
            sql = text(f"DELETE FROM {table}")
            self._db.session.execute(sql)
            self._db.session.commit()

    def delete_bibtex(self, ref_id: int):
        sql = text("DELETE FROM bibtex WHERE id = :id")
        self._db.session.execute(sql, {"id": ref_id})
        self._db.session.commit()

bibtex_repository = BibtexRepository(db)
