import json

from tests import MercuryAppTestCase


class TodoTest(MercuryAppTestCase):

    def test_todos(self):
        self.login()
        create_response = self.client.post("/todos", data={"title": "hello", "description": "world"})

        self.assertEquals(create_response.status, '201 CREATED')

        response = self.client.get("/todos")
        response_json = json.loads(response.data)

        self.assertEquals(response_json, dict(todos=[{"id": 1, "title": "hello", "description": "world"}]))