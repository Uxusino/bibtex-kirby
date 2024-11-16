from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.bibtex_repository import bibtex_repository as repo
from config import app, test_env

@app.route("/")
def index():
    bibtexs = repo.get_bibtexs()
    return render_template("index.html", bibtexs=bibtexs) 

# TODO: replace dummy content with normal content
@app.route("/create_bibtex", methods=["POST"])
def bibtex_creation():
    label = request.form.get("label")

    content = {
        "label": label,
        "type": "article",
        "data": None
    }

    try:
        repo.create_bibtex(content)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
