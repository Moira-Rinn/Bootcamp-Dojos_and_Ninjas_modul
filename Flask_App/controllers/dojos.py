from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.dojo import Dojo
from Flask_App.models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form['dojo_name']
    }
    Dojo.save(data)
    return redirect('/dojos')


@app.route('/dojos')
def dojo():
    query = "SELECT * FROM dojos;"
    dojos = Dojo.get_all(query)
    return render_template("index.html", dojos=dojos)


@app.route('/show/<int:dojo_id>')
def detail_page(dojo_id):
    dQuery = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
    dData = {
        'id': dojo_id
    }

    nQuery = "SELECT * FROM ninjas;"

    dResults = Dojo.get_all(dQuery, dData)
    nResults = Ninja.get_all(nQuery)

    return render_template("details_page.html", dojo=dResults[0], ninjas=nResults)


# @app.route('/edit_page/<int:user_id>')
# def edit_page(user_id):
#     query = "SELECT * FROM users WHERE id = %(id)s;"
#     data = {
#         'id': user_id
#     }
#     user = User.get_all(query, data)
#     print(user)
#     return render_template("edit_page.html", user=user[0])


# @app.route('/update/<int:user_id>', methods=['POST'])
# def update(user_id):
#     query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
#     data = {
#         'id': user_id,
#         "fname": request.form['fname'],
#         "lname": request.form['lname'],
#         "email": request.form['email']
#     }
#     user = User.edit_user(query, data)
#     print(user)
#     return redirect(f"/show/{user_id}")


# @app.route('/delete/<int:user_id>')
# def remove_user(user_id):
#     query = "DELETE FROM users WHERE id = %(id)s;"
#     data = {
#         'id': user_id,
#     }
#     User.remove_user(query, data)
#     return redirect('/users')
