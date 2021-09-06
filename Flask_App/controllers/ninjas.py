from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.ninja import Ninja
from Flask_App.models.dojo import Dojo


@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo']
    }
    Ninja.save(data)

    return redirect('/show_ninjas')


@app.route('/add_ninja')
def add_ninja():
    dQuery = 'SELECT * FROM dojos;'
    dojos = Dojo.get_all(dQuery)
    return render_template("add_ninja.html", dojos=dojos)


@app.route('/show_ninja/<int:ninja_id>')
def show_ninja(ninja_id):
    query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
    data = {
        'id': ninja_id
    }

    results = Ninja.get_all(query, data)

    return render_template("show_ninja.html", ninja=results[0])


@app.route('/show_ninjas')
def show_ninjas():
    nQuery = "SELECT * FROM ninjas;"
    dQuery = "SELECT * FROM dojos;"

    ninjas = Ninja.get_all(nQuery)
    dojos = Dojo.get_all(dQuery)

    return render_template("show_ninjas.html", ninjas=ninjas, dojos=dojos)


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


@app.route('/delete/<int:ninja_id>')
def remove_ninja(ninja_id):
    query = "DELETE FROM ninjas WHERE id = %(id)s;"
    data = {
        'id': ninja_id,
    }
    Ninja.remove_ninja(query, data)
    return redirect('/show_ninjas')
