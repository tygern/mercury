from flask import session
from mercury.authentication import AuthenticationService
from mercury.todo import TodoService

todo_service = TodoService()
authentication_service = AuthenticationService(session)