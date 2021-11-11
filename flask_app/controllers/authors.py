# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_author import Author
from flask_app.models.model_book import Book


@app.route('/')
def authors():
    authors = Author.get_all()
    return render_template("authors.html", authors=authors)

@app.route('/author/create', methods=['POST'])
def create_author():
    print(request.form)
    Author.create(request.form)
    return redirect('/')

@app.route('/author_info/<int:id>')
def authorInfo(id):
    data = { 'id' : id }
    session['author_id'] = id
    author = Author.get_one_with_books(data)
    books = Book.get_all()
    return render_template('author_info.html', author = author, books = books)

@app.route('/add_favorite', methods = ['POST'])
def add_favorite():
    Author.create_favorite(request.form)
    id = session['author_id']
    return redirect(f'/author_info/{id}')
