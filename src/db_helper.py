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

table_name = "bibtex"

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
    f" WHERE table_name = '{name}'"
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
  rows from the table specified by the global variable `table_name`. After
  executing the statement, it commits the transaction to the database.

  Raises:
    SQLAlchemyError: If there is an error executing the SQL statement or committing the transaction.
  """
  print(f"Clearing contents from table {table_name}")
  sql = text(f"DELETE FROM {table_name}")
  db.session.execute(sql)
  db.session.commit()

def setup_db():
  """
  Sets up the database by dropping the existing table if it exists and creating a new one.

  This function checks if a table with the specified name exists. If it does, the table is dropped.
  Then, a new table with the same name is created with the following columns:
  - id: A serial primary key.
  - label: A unique text field that cannot be null.
  - type: A text field that cannot be null.
  - creation_time: A timestamp field.
  - modified_time: A timestamp field.
  - data: A JSON field.

  The function commits the changes to the database after executing the SQL commands.
  """
  if table_exists(table_name):
    print(f"Table {table_name} exists, dropping")
    sql = text(f"DROP TABLE {table_name}")
    db.session.execute(sql)
    db.session.commit()

  # Label must be unique
  print(f"Creating table {table_name}")
  sql = text(
    f'CREATE TABLE "{table_name}" ('
    "  id SERIAL PRIMARY KEY, "
    "  label TEXT NOT NULL UNIQUE, "
    "  type TEXT NOT NULL, "
    "  creation_time TIMESTAMP, "
    "  modified_time TIMESTAMP, "
    "  data JSON "
    ")"
  )

  db.session.execute(sql)
  db.session.commit()

if __name__ == "__main__":
    with app.app_context():
      setup_db()
