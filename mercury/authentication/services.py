class AuthenticationService:
    def __init__(self, session, g, oid, user_service):
        self.session = session
        self.g = g
        self.oid = oid
        self.user_service = user_service

    def external_login(self):
        return self.oid.try_login('https://www.google.com/accounts/o8/id', ask_for=['email', 'nickname'],
                           ask_for_optional=['fullname'])

    def login(self, user):
        self.session['openid'] = user.openid
        self.g.user = user

    def logout(self):
        self.g.user = None
        self.session.pop('openid', None)

    def logged_in(self):
        return self.g.user is not None

    def set_current_user(self):
        self.g.user = None
        if 'openid' in self.session:
            openid = self.session['openid']
            self.g.user = self.user_service.find_by(openid=openid)