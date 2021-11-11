# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_book

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ***CREATE***
    @classmethod
    def create(cls,data):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        author_id = connectToMySQL('books').query_db(query,data)
        return author_id

    @classmethod
    def create_favorite(cls,data):
        query = " INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        new_favorite = connectToMySQL('books').query_db(query, data)
        return new_favorite

    # # ***Retreive***

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books').query_db(query)
        return results 

	# # (joining two groups)  
    # # add... from .model_(user/no()) import (User/no()) **to top of page 
	# # add... self.(users/no()) = [] **to class(User/no()):
    @classmethod
    def get_one_with_books(cls, data ):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books').query_db(query,data)
        author = cls(results[0])
        author.books = []
        for row in results:
            book_data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at']
            }
            author.books.append( model_book.Book(book_data) )
        return author




    #    **** UPDATE****

