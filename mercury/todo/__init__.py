from mercury import db
from mercury.services import CrudService
from mercury.todo.models import Todo

todo_service = CrudService(Todo, db.session)