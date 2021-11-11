# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    # ***CREATE***
    @classmethod
    def create(cls,data):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        author_id = connectToMySQL('books').query_db(query,data)
        return author_id

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
    def get_one_with_favorites_m2m(cls, data ):
        print(data)
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(data)s;"
        results = connectToMySQL('books').query_db(query,data)
        author = cls(results[0])
        print(author)
        for row in results:
            a = {
                'id': row['author.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            # users = [] in self dictionary
            dojo.authors.append( Author(a) )
        return dojo
