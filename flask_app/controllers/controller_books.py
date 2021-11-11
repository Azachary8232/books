from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_book import Book 
from flask_app.models.model_author import Author


@app.route('/books')
def books():
    books = Book.get_all()
    return render_template('books.html', books = books)

@app.route('/create_book', methods = ['POST'])
def create_book():
    Book.create(request.form)
    return redirect('/books')

@app.route('/book_info/<int:id>')
def book_info(id):
    data = {'id' : id }
    book = Book.get_book_with_many(data)
    authors = Author.get_all()
    return render_template('book_info.html', book = book, authors = authors)


@app.route('/add_book_fav', methods = ['POST'])
def add_book_fav():
    print('!!!')
    print(request.form)
    Author.create_favorite(request.form)
    id = request.form['book_id']
    return redirect(f'/book_info/{id}')