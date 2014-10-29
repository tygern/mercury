import json
from tests import MercuryAppTestCase


class TodoTest(MercuryAppTestCase):

    def test_todos(self):
        unauthenticated_response = self.client.post("/todos", data={"title": "hello", "description": "world"})
        self.assertEquals(unauthenticated_response.status, '401 UNAUTHORIZED')

        login_response = self.login('admin', 'default')
        self.assertEquals(login_response.status, '200 OK')

        login_response_json = json.loads(login_response.data)
        self.assertTrue(login_response_json['success'])

        create_response = self.client.post("/todos", data={"title": "hello", "description": "world"})
        self.assertEquals(create_response.status, '200 OK')