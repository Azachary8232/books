# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_author import Author

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all()
    return render_template("authors.html", authors=authors)

# @app.route('/create/(user/no())', methods=['POST'])
# def create_author():
#     data = {
#         # 'id' : id
#         "(something/no())" : requestform['(somethong/no())']
#     }
#     Author.create(data)
#     return redirect('author_info')

# # Left Join
# @app.route('/dojo/<int:id>')
# def dojo(id):
#     data = {
#     "id": id
#     }
#     return render_template('dojo_info.html', dojo=Author.get_one_with_ninjas(data))   