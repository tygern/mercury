from mercury import app


class AuthenticationService:
    def __init__(self, session):
        self.session = session

    def login(self, username, password):
        error = None
        if username != app.config['USERNAME']:
            error = 'Invalid username'
        elif password != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            self.session['logged_in'] = True

        return {
            "success": error is None,
            "message": error
        }

    def logout(self):
        self.session.pop('logged_in', None)
        return {
            "success": True
        }