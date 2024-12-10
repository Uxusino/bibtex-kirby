"""
Tämä moduuli tarjoaa apufunktioita tietokannan käsittelyyn.

Funktiot:
  table_exists(name):
    Tarkistaa, onko tietokantataulu olemassa.
    Parametrit:
      name (str): Taulun nimi.
    Palauttaa:
      bool: True, jos taulu on olemassa, muuten False.

  reset_db():
    Tyhjentää tietokantataulun sisällön.

  setup_db():
    Luo tietokantataulun, jos se ei ole olemassa, tai pudottaa ja luo sen uudelleen
    jos se on olemassa.
"""
from sqlalchemy import text
from config import db, app
from repositories.bibtex_repository import bibtex_repository as repo
from dotenv import load_dotenv
import os

load_dotenv()
DEMO_MODE = os.getenv('DEMO_MODE', 'False') == 'True'
TABLE_NAMES = ["bibtex", "tags"]

def table_exists(name):
  """
  Check if a table with the given name exists in the database.

  Args:
    name (str): The name of the table to check.

  Returns:
    bool: True if the table exists, False otherwise.
  """
  sql_table_existence = text(
    "SELECT EXISTS ("
    "  SELECT 1"
    "  FROM information_schema.tables"
    f" WHERE TABLE_NAME = '{name}'"
    ")"
  )

  print(f"Checking if table {name} exists")
  print(sql_table_existence)

  result = db.session.execute(sql_table_existence)
  return result.fetchall()[0][0]

def reset_db():
  """
  Clears all contents from the specified table in the database.

  This function constructs and executes a SQL DELETE statement to remove all
  rows from the table specified by the global variable `TABLE_NAME`. After
  executing the statement, it commits the transaction to the database.

  Raises:
    SQLAlchemyError: If there is an error executing the SQL statement or committing the transaction.
  """
  for table in TABLE_NAMES:
    print(f"Clearing contents from table {table}")
    sql = text(f"DELETE FROM {table}")
    db.session.execute(sql)
    db.session.commit()

def setup_db():
  for table in TABLE_NAMES:
    if table_exists(table):
      print(f"Table {table} exists, dropping")
      sql = text(f"DROP TABLE {table}")
      db.session.execute(sql)
      db.session.commit()

    print(f"Creating table {table}")
    if table == "bibtex":
      sql = text(
        f'CREATE TABLE "{table}" ('
        "  id SERIAL PRIMARY KEY, "
        "  label TEXT NOT NULL, "
        "  type TEXT NOT NULL, "
        "  creation_time TIMESTAMP, "
        "  modified_time TIMESTAMP, "
        "  data JSON "
        ")"
      )
    if table == "tags":
      sql = text(
        f'CREATE TABLE "{table}" ('
        "  id SERIAL PRIMARY KEY, "
        "  name TEXT NOT NULL, "
        "  bibtex_id SMALLINT "
        ")"
      )

    db.session.execute(sql)
    db.session.commit()

  if DEMO_MODE:
    print("Demo mode on: creating bibtexs:")
    for i in range(100):
      print(f"{i+1}/100")
      repo.create_bibtex({
        'label': f'd_m_{i+1}',
        'type': 'article',
        'data': {
          'title': f'Demo {i+1}',
          'author': 'Mr. Demo',
          'journal': 'Demo.com',
          'year': '2020'
        },
        'tags': None
      })
    print("ready")

if __name__ == "__main__":
    with app.app_context():
      setup_db()
