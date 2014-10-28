from flask import session, abort, request, jsonify
from mercury import app, db
from mercury.todo.models import Todo


@app.route('/todos', methods=['GET'])
def show_todos():
    todos = Todo.query.all()
    return jsonify(todos=[t.serialize for t in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    if not session.get('logged_in'):
        abort(401)
    todo = Todo(request.form['title'], request.form['description'])
    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.serialize)
