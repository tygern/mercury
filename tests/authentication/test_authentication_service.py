from mercury.authentication import AuthenticationService
from tests import MercuryTestCase


class TestAuthenticationService(MercuryTestCase):
    def test_logged_in(self):
        authentication_service = AuthenticationService({'logged_in': True})

        self.assertEquals(authentication_service.logged_in(), True)

    def test_logged_in_logged_out(self):
        authentication_service = AuthenticationService({})

        self.assertEquals(authentication_service.logged_in(), False)

    def test_logout(self):
        session = {'logged_in': True}
        AuthenticationService(session).logout()

        self.assertEquals(session.get('logged_in'), None)

    def test_login(self):
        session = {}
        result = AuthenticationService(session).login('admin', 'default')

        self.assertEquals(session.get('logged_in'), True)
        self.assertEquals(result['success'], True)

    def test_login_bad_username(self):
        session = {'logged_in': 'anything'}
        result = AuthenticationService(session).login('badUsername', 'default')

        self.assertEquals(session.get('logged_in'), None)
        self.assertEquals(result['success'], False)
        self.assertEquals(result['message'], 'Invalid login')

    def test_login_bad_password(self):
        session = {'logged_in': 'anything'}
        result = AuthenticationService(session).login('admin', 'badPassword')

        self.assertEquals(session.get('logged_in'), None)
        self.assertEquals(result['success'], False)
        self.assertEquals(result['message'], 'Invalid login')
