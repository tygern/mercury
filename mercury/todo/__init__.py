from mercury import db
from mercury.todo.models import Todo


class TodoService:
    def find_all(self):
        return Todo.query.all()

    def create(self, title, description):
        todo = Todo(title, description)
        db.session.add(todo)
        db.session.commit()

        return todo
