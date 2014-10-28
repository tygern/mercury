from mercury import db
from mercury.todo.models import Todo


class TodoRepository:
    def __init__(self):
        self.db = db

    def create(self, session, todo):
        session.add(todo)

        return todo

    def find_all(self):
        return Todo.query.all()
