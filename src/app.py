from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.bibtex_repository import bibtex_repository as repo
from config import app, test_env
from util import parse_request

@app.route("/", defaults={"sort": "creation_time=1"})
@app.route("/<sort>/")
def index(sort):
    sort, reverse = sort.split("=")
    bibtexs = repo.get_bibtexs()
    if sort == "label":
        bibtexs.sort(key=lambda x: x.label.split("_")[1], reverse=int(reverse))
    else:
        bibtexs.sort(key=lambda x: getattr(x, sort), reverse=int(reverse))
    return render_template("index.html", bibtexs=bibtexs) 

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create_bibtex", methods=["POST"])
def bibtex_creation():
    content = request.form.to_dict()
    
    try:
        new_bib = parse_request(content)
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

# TODO: make possible to add missing fields in the future
@app.route("/update_bibtex", methods=["POST"])
def update_bibtex():
    content = request.form.to_dict()
    id = int(content.get("bibtex_id"))
    del content['bibtex_id']

    try:
        upd_bib = parse_request(content)
        repo.update_bibtex(id, upd_bib)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
