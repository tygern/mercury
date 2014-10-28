from unittest import TestCase
from mercury import db, app


class MercuryTestCase(TestCase):
    pass


class MercuryAppTestCase(MercuryTestCase):

    def _create_app(self):
        # app = Flask(__name__)
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

    def login(self, username=None, password=None):
        return self.client.post('/login', data={'username': username, 'password': password})