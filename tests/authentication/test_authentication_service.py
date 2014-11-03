from mock import MagicMock
from mercury.authentication import AuthenticationService
from tests import MercuryTestCase


class TestAuthenticationService(MercuryTestCase):
    def setUp(self):
        self.session = {}
        self.g = MagicMock()
        self.oid = MagicMock()
        self.oid.try_login = MagicMock()
        self.user_service = MagicMock()
        self.user_service.find_by = MagicMock()

    def test_external_login(self):
        AuthenticationService(self.session, self.g, self.oid, self.user_service).external_login()

        self.oid.try_login.assert_called_with('https://www.google.com/accounts/o8/id',
                                              ask_for=['email', 'nickname'], ask_for_optional=['fullname'])

    def test_login(self):
        self.session['openid'] = None

        user = MagicMock()
        user.openid = '1234'
        self.g.user = None

        AuthenticationService(self.session, self.g, self.oid, self.user_service).login(user)

        self.assertEquals(self.session['openid'], '1234')
        self.assertEquals(self.g.user, user)

    def test_logout(self):
        self.session['openid'] = '1234'
        self.g.user = 'user'

        AuthenticationService(self.session, self.g, self.oid, self.user_service).logout()

        self.assertFalse('openid' in self.session)
        self.assertIsNone(self.g.user)

    def test_logged_in_true(self):
        self.g.user = 'user'
        authentication_service = AuthenticationService(self.session, self.g, self.oid, self.user_service)
        self.assertTrue(authentication_service.logged_in())

    def test_logged_in_false(self):
        self.g.user = None
        authentication_service = AuthenticationService(self.session, self.g, self.oid, self.user_service)
        self.assertFalse(authentication_service.logged_in())

    def test_set_current_user_logged_out(self):
        self.g.user = 'user'
        AuthenticationService(self.session, self.g, self.oid, self.user_service).set_current_user()
        self.assertIsNone(self.g.user)

    def test_set_current_user_logged_in(self):
        self.session['openid'] = '1234'
        self.g.user = None
        self.user_service.find_by.return_value = 'user'

        AuthenticationService(self.session, self.g, self.oid, self.user_service).set_current_user()

        self.assertEquals(self.g.user, 'user')
        self.user_service.find_by.assert_called_with(openid='1234')