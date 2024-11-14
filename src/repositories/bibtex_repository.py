from config import db
from sqlalchemy import text

from entities.bibtex import Bibtex

def get_bibtexs():
    #todo fiksaa nää
    result = db.session.execute(text("SELECT id, content FROM bibtex"))
    bibtexs = result.fetchall()
    return bibtexs

def create_bibtex(content):
    #todo fiksaa nää
    sql = text("INSERT INTO bibtex (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()
