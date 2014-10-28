from mercury import app


class AuthenticationService:
    def __init__(self, session):
        self.session = session

    def login(self, username, password):
        error = None
        if username != app.config['USERNAME'] or password != app.config['PASSWORD']:
            error = 'Invalid login'
            self.__logout_from_session()
        else:
            self.session['logged_in'] = True

        return {
            "success": error is None,
            "message": error
        }

    def logout(self):
        self.__logout_from_session()
        return {
            "success": True
        }

    def logged_in(self):
        return self.session.get('logged_in') == True

    def __logout_from_session(self):
        self.session.pop('logged_in', None)
