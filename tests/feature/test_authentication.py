from tests import MercuryAppTestCase


class AuthenticationTest(MercuryAppTestCase):

    def test_authentication(self):
        unauthenticated_response = self.client.post("/todos", data={"title": "hello", "description": "world"})
        self.assertEquals(unauthenticated_response.status, '401 UNAUTHORIZED')

        unauthenticated_redirect = self.client.get("/")
        self.assertEquals(unauthenticated_redirect.status, '302 FOUND')
        self.assertRegexpMatches(unauthenticated_redirect.location, '/login$')

        self.login()

        create_response = self.client.post("/todos", data={"title": "hello", "description": "world"})
        self.assertEquals(create_response.status, '201 CREATED')

        index_response = self.client.get("/")
        self.assertEquals(index_response.status, '200 OK')