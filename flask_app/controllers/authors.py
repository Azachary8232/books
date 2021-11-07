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

@app.route('/author/create', methods=['POST'])
def create_author():
    print(request.form)
    id = Author.create(request.form)
    return redirect('/authors')



# # Left Join
# @app.route('/dojo/<int:id>')
# def dojo(id):
#     data = {
#     "id": id
#     }
#     return render_template('dojo_info.html', dojo=Author.get_one_with_ninjas(data))   