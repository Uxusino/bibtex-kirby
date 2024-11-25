from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.bibtex_repository import bibtex_repository as repo
from config import app, test_env
from util import parse_request

# Filter to turn bibtexes to strings inside the template
@app.template_filter('to_str')
def to_str(bibtex):
    return str(bibtex)

@app.route("/", defaults={"sort": "creation_time=1"})
@app.route("/<sort>/")
def index(sort):
    sort, reverse = sort.split("=")
    bibtexs = repo.get_bibtexs()
    if sort == "label":
        bibtexs.sort(key=lambda x: x.data["title"], reverse=int(reverse))
    else:
        bibtexs.sort(key=lambda x: getattr(x, sort), reverse=int(reverse))
    return render_template("index.html", bibtexs=bibtexs) 

@app.route("/create_article")
def create_article():
    return render_template("create_article.html")

@app.route("/create_book")
def create_book():
    return render_template("create_book.html")

@app.route("/create_inproceedings")
def create_inproceedings():
    return render_template("create_inproceedings.html")

@app.route("/create_misc")
def create_misc():
    return render_template("create_misc.html")

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
    
@app.route("/export")
def export():
    file_content = ""
    bibtexes = repo.get_bibtexs()
    for bib in bibtexes:
        file_content = file_content + str(bib) + "\n\n"

    return Response(
        file_content,
        mimetype="text/plain",
        headers={
            "Content-Disposition": "attachment;filename=bibliography.bib"
        }
    )


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
