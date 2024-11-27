"""
This module defines the routes and views for a Flask web application that manages BibTeX entries.
Dependencies:
    Flask: Used for routing and rendering templates.
    db_helper: Contains the function to reset the database.
    repositories.bibtex_repository: Provides access to the BibTeX repository.
    config: Contains the Flask app configuration and environment settings.
    util: Contains utility functions, including request parsing.
"""
from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.bibtex_repository import bibtex_repository as repo
from config import app, test_env
from util import parse_request

# Filter to turn bibtexes to strings inside the template
@app.template_filter('to_str')
def to_str(bibtex):
    """
    Convert a BibTeX entry to its string representation.

    Args:
        bibtex: The BibTeX entry to be converted.

    Returns:
        str: The string representation of the BibTeX entry.
    """
    return str(bibtex)

@app.route("/", defaults={"sort": "creation_time=1"})
@app.route("/<sort>/")
def index(sort):
    """
    Display the index page with a list of BibTeX entries, sorted by the specified criteria.
    Args:
        sort (str): The sorting criteria and order, formatted as "criteria=order".
                    For example, "creation_time=1" sorts by creation time in ascending order.

    Returns:
        Response: The rendered index page with the sorted list of BibTeX entries.
    """
    if "=" in sort:
        sort, reverse = sort.split("=")
        reverse = int(reverse)
    else:
        sort, reverse = "creation_time", 1

    bibtexs = repo.get_bibtexs()
    if sort == "label":
        bibtexs.sort(key=lambda x: x.data["title"].lower(), reverse=reverse)
    else:
        bibtexs.sort(key=lambda x: getattr(x, sort), reverse=reverse)
    return render_template("index.html", bibtexs=bibtexs)

@app.route("/search", methods = ["POST"])
def search():
    query = request.form["query"]
    if len(query) > 100:
        return ("Query too long")
    return redirect(f"/search/{query}")

@app.route("/search/<query>")
def search_releases(query):
    bibtexs = repo.get_bibtexs()
    bibtexs = list(filter(lambda b: query.lower() in b.data["author"].lower()
                          or query.lower() in b.data["title"].lower(), bibtexs))
    return render_template("/search.html", bibtexs=bibtexs, search=query)

@app.route("/create_article")
def create_article():
    """
    Renders the template for creating a new article.

    Returns:
        Response: The rendered HTML template for creating an article.
    """
    return render_template("create_article.html")

@app.route("/create_book")
def create_book():
    """
    Renders the template for creating a book.

    Returns:
        Response: The rendered HTML template for creating a book.
    """
    return render_template("create_book.html")

@app.route("/create_inproceedings")
def create_inproceedings():
    """
    Renders the template for creating an inproceedings entry.

    Returns:
        A rendered HTML template for creating an inproceedings entry.
    """
    return render_template("create_inproceedings.html")

@app.route("/create_misc")
def create_misc():
    """
    Renders the 'create_misc.html' template.

    Returns:
        Response: The rendered HTML template for creating miscellaneous entries.
    """
    return render_template("create_misc.html")

@app.route("/create_bibtex", methods=["POST"])
def bibtex_creation():
    """
    Handles the creation of a new BibTeX entry from a form submission.
    This function retrieves form data, parses it into a BibTeX entry, and 
    attempts to save it to the repository. If an error occurs during the 
    process, it flashes the error message and redirects the user back to 
    the creation page for the specific entry type.
    Returns:
        Response: A redirect response to the home page on success, or to the 
        creation page with an error message on failure.
    """
    content = request.form.to_dict()
    type = content.get("type")
    
    try:
        new_bib = parse_request(content)
        repo.create_bibtex(new_bib)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/create_" + type)
    
@app.route("/delete_bibtex", methods=["POST"])
def delete_bibtex():
    """
    Deletes a BibTeX entry from the repository.

    This function retrieves the BibTeX ID from the form data submitted via a POST request,
    deletes the corresponding BibTeX entry from the repository, and then redirects the user
    to the home page.

    Returns:
        Response: A redirect response to the home page.
    """
    bib_tex_id = request.form.get("bibtex_id")
    repo.delete_bibtex(bib_tex_id)
    return redirect("/")

# TODO: make possible to add missing fields in the future
@app.route("/update_bibtex", methods=["POST"])
def update_bibtex():
    """
    Handles the update of an existing BibTeX entry from a form submission.
    
    This function retrieves form data, parses it into a BibTeX entry, and 
    attempts to update the existing entry in the repository. If an error 
    occurs during the process, it flashes the error message and redirects 
    the user back to the home page.
    
    Returns:
        Response: A redirect response to the home page on success or failure.
    """
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
    """
    Export all BibTeX entries from the repository as a plain text file.

    This function retrieves all BibTeX entries from the repository, concatenates
    them into a single string with double newline separators, and returns a 
    Flask Response object to prompt the user to download the content as a 
    .bib file.

    Returns:
        Response: A Flask Response object containing the BibTeX entries as a 
        plain text file with the filename 'bibliography.bib'.
    """
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
        """
        Resets the database by calling the reset_db function and returns a JSON response.

        Returns:
            Response: A JSON response with a message indicating that the database has been reset.
        """
        reset_db()
        return jsonify({ 'message': "db reset" })
