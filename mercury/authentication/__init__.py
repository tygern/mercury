from flask import session, g
from mercury import oid
from mercury.authentication.services import AuthenticationService
from mercury.user import user_service

authentication_service = AuthenticationService(session, g, oid, user_service)
