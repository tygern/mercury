from flask import request, render_template

from mercury import app
from mercury.control import requires_auth
from mercury.serializers import serialize, serialize_list
from mercury.todo import todo_service


@app.route('/', methods=['GET'])
@requires_auth(api=False)
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
@requires_auth()
def show_todos():
    todos = todo_service.find_all()

    return serialize_list('todos', todos)

@app.route('/todos', methods=['POST'])
@requires_auth()
def add_todo():
    todo = todo_service.create(title=request.form['title'], description=request.form['description'])
    response = serialize(todo)
    response.status_code = 201
    return response
