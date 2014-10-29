from flask import session
from mercury import db
from mercury.authentication import AuthenticationService

from mercury.todo.models import Todo

class CrudService:
    def __init__(self, model_class, db_session):
        self.db_session = db_session
        self.model_class = model_class

    def find_all(self):
        return self.model_class.query.all()

    def create(self, **kwargs):
        todo = self.model_class(**kwargs)
        self.db_session.add(todo)
        self.db_session.commit()

        return todo

todo_service = CrudService(Todo, db.session)
authentication_service = AuthenticationService(session)