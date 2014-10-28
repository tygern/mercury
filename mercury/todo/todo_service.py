from mercury.persistence.session import Session
from mercury.todo.models import Todo
from mercury.todo.todo_repository import TodoRepository


class TodoService:
    def __init__(self):
        self.repository = TodoRepository()

    def find_all(self):
        return self.repository.find_all()

    def create(self, title, description):
        with Session(self.repository.db) as session:
            todo = self.repository.create(session, Todo(title, description))

        return todo