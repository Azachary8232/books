from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_author



class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    # ***CREATE***
    @classmethod
    def create(cls,data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        book_id = connectToMySQL('books').query_db(query,data)
        return book_id


    #  ***Retreive***

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books').query_db(query)
        return results 

    @classmethod
    def get_book_with_many(cls, data):
        query =  "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)
        book = cls(results[0])
        book.authors = []
        for row in results:
            author_data = {
                'id' : row['authors.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'created_at' : row['authors.created_at'],
                'updated_at' : row['authors.created_at']
            }
            book.authors.append(model_author.Author(author_data))
        return book

    