# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.(user/no()) import (User/no())

@app.route('/')
def users():
    return render_template('index.html')

@app.route('/create/(user/no())', methods=['POST'])
def create_(user/no())():
    data = {
        # 'id' : id
        "(something/no())" : requestform['(somethong/no())']
    }
    (User/no()).create(data)
    return redirect('/*user*)')

# Left Join
@app.route('/dojo/<int:id>')
def dojo(id):
    data = {
    "id": id
    }
    return render_template('dojo_info.html', dojo=Dojo.get_one_with_ninjas(data))   