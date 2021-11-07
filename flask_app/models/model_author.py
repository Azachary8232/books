# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ***CREATE***
    # @classmethod
    # def create(cls,data):
    #     query = "INSERT INTO (users/no()) (*something*, *something*) VALUES (%(*something*)s, %(*something*)s;"
    #     author_id = connectToMySQL('(userS/no())').query_db(query,data)
    #     return author_id

    # # ***Retreive***

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors 

	# # (joining two groups)  
    # # add... from .model_(user/no()) import (User/no()) **to top of page 
	# # add... self.(users/no()) = [] **to class(User/no()):
    # @classmethod
    # def get_one_with_ninjas(cls, data ):
    #     print(data)
    #     query = "SELECT * FROM (userS/no()) LEFT JOIN ninjas on (userS/no()).id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
    #     results = connectToMySQL('***userS***').query_db(query,data)
    #     dojo = cls(results[0])
    #     for row in results:
    #         n = {
    #             'id': row['ninjas.id'],
    #             'first_name': row['first_name'],
    #             'last_name': row['last_name'],
    #             'age': row['age'],
    #             'created_at': row['ninjas.created_at'],
    #             'updated_at': row['ninjas.updated_at']
    #         }
    #         # users = [] in self dictionary
    #         dojo.authors.append( Author(n) )
    #     return dojo
