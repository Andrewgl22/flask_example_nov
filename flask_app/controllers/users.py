from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User

@app.route('/html')
def html():
    users = User.get_all()
    return render_template('index.html', users = users)

@app.route('/user/new')
def form():
    return render_template('form.html')

@app.route('/user', methods=['POST'])
def create_user():
    print(request.form)

    data = {
        "username": request.form['username'],
        "email": request.form['email'],
        "age": request.form['age'],
        "country": request.form['country']
    }

    User.save(data)
    return redirect('/html')

@app.route('/user/<int:id>')
def one_user(id):
    data = {
        "id":id
    }
    user = User.get_one_by_id(data)
    return render_template('one_user.html', user=user)

@app.route('/user/<int:id>/edit')
def edit_form(id):
    data = {
        "id":id
    }
    user = User.get_one_by_id(data)
    return render_template('edit.html',user=user)

@app.route('/user/<int:id>/edit', methods=['POST'])
def edit_user(id):
    data = {
        "id":id,
        "username": request.form['username'],
        "email": request.form['email'],
        "age": request.form['age'],
        "country": request.form['country']
    }
    User.edit_user(data)
    return redirect('/html')

@app.route('/user/<int:id>/delete')
def delete_user(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/html')


