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
    print('!!!')
    Book.create(request.form)
    return redirect('/books')
