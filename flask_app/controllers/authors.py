# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_author import Author


@app.route('/')
def authors():
    authors = Author.get_all()
    return render_template("authors.html", authors=authors)

@app.route('/author/create', methods=['POST'])
def create_author():
    Author.create(request.form)
    return redirect('/')

@app.route('/author_info/<int:id>')
def authorInfo(id):
    id_data = { 'id' : id }
    author_data = Author.get_one_with_favorites_m2m(id_data)
    return render_template('author_info.html', author_data)


