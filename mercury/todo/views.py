from flask import session, abort, request, jsonify
from mercury import app
from mercury.todo.todo_service import TodoService


@app.route('/todos', methods=['GET'])
def show_todos():
    todos = TodoService().find_all()
    return jsonify(todos=[t.serialize for t in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    if not session.get('logged_in'):
        abort(401)

    todo = TodoService().create(request.form['title'], request.form['description'])

    return jsonify(todo.serialize)
