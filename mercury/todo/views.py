from flask import render_template, session, abort, request, flash, redirect, url_for
from mercury import app, db
from mercury.todo.models import Todo


@app.route('/')
def show_todos():
    todos = Todo.query.all()
    return render_template('show_todos.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    if not session.get('logged_in'):
        abort(401)
    todo = Todo(request.form['title'], request.form['description'])
    db.session.add(todo)
    db.session.commit()

    flash('New todo was successfully posted')
    return redirect(url_for('show_todos'))