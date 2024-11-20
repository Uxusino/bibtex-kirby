from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.bibtex_repository import bibtex_repository as repo
from config import app, test_env
from util import validate_data, generate_label

@app.route("/")
def index():
    bibtexs = repo.get_bibtexs()
    return render_template("index.html", bibtexs=bibtexs) 

@app.route("/create")
def create():
    return render_template("create.html")

# TODO: make possible to add other types of references
@app.route("/create_bibtex", methods=["POST"])
def bibtex_creation():
    content = request.form.to_dict()

    # Removes empty fields
    data = {k: v for k, v in content.items() if v}
    label = generate_label(data)

    new_bib = {
        "label": label,
        "type": "article",
        "data": data
    }

    try:
        validate_data(content)
        repo.create_bibtex(new_bib)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/create")
    
@app.route("/delete_bibtex", methods=["POST"])
def delete_bibtex():
    bib_tex_id = request.form.get("bibtex_id")
    repo.delete_bibtex(bib_tex_id)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
