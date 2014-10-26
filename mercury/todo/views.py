from flask import g, render_template
from mercury import app

@app.route('/')
def show_todos():
    cur = g.db.execute('select title, description from todo order by id desc')
    todos = [{'title': row[0], 'description': row[1]} for row in cur.fetchall()]
    return render_template('show_todos.html', todos=todos)