from flask import session, abort, request
from mercury import app
from mercury.serializers import serialize, serialize_list
from mercury.services import todo_service, authentication_service


@app.route('/todos', methods=['GET'])
def show_todos():
    todos = todo_service.find_all()

    return serialize_list('todos', todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    if not authentication_service.logged_in():
        abort(401)

    todo = todo_service.create(title=request.form['title'], description=request.form['description'])
    response = serialize(todo)
    response.status_code = 201
    return response
