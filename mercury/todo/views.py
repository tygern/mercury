from flask import g, render_template, session, abort, request, flash, redirect, url_for
from mercury import app

@app.route('/')
def show_todos():
    cur = g.db.execute('select title, description from todo order by id desc')
    todos = [{'title': row[0], 'description': row[1]} for row in cur.fetchall()]
    return render_template('show_todos.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into todo (title, description) values (?, ?)',
                 [request.form['title'], request.form['description']])
    g.db.commit()
    flash('New todo was successfully posted')
    return redirect(url_for('show_todos'))