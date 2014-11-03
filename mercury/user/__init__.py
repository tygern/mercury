from mercury import db
from mercury.services import CrudService
from mercury.user.models import User

user_service = CrudService(User, db.session)