from unittest import TestCase
from mercury import db, app
from mercury.user.models import User


class MercuryTestCase(TestCase):
    pass


class MercuryAppTestCase(MercuryTestCase):

    def _create_app(self):
        app.config.from_object("config.TestConfig")
        app.config['LIVESERVER_PORT'] = 8943
        app.config['SERVER_NAME'] = 'localhost:8943'
        return app

    def setUp(self):
        super(MercuryTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        super(MercuryAppTestCase, self).tearDown()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self):
        user = User("Fred", "fred@example.com", "http://www.example.com/some/open/id/1234")
        db.session.add(user)
        db.session.commit()

        with self.client.session_transaction() as session:
            session['openid'] = user.openid

    def logout(self):
        with self.client.session_transaction() as session:
            session.pop('openid', None)