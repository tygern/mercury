from mock import patch
from mercury.authentication.views import login, logout
from tests import MercuryTestCase


class TestAuthenticationViews(MercuryTestCase):
    def setUp(self):
        self.jsonify_patcher = patch('mercury.authentication.views.jsonify')
        self.mock_jsonify = self.jsonify_patcher.start()
        
        self.authentication_service_patcher = patch('mercury.authentication.views.authentication_service')
        self.mock_authentication_service = self.authentication_service_patcher.start()

    def tearDown(self):
        self.jsonify_patcher.stop()
        self.authentication_service_patcher.stop()

    def test_logout(self):
        attrs = {"logout.return_value": {"success": True}}
        self.mock_authentication_service.configure_mock(**attrs)
        self.mock_jsonify.return_value = "json"

        result = logout()

        self.assertEquals(result, "json")
        self.mock_jsonify.assert_called_with({"success": True})

    @patch('mercury.authentication.views.request')
    def test_login(self, mock_request):
        mock_request.form = {"username": "username", "password": "password"}

        attrs = {"login.return_value": {"success": True}}
        self.mock_authentication_service.configure_mock(**attrs)
        self.mock_jsonify.return_value = "json"

        result = login()

        self.assertEquals(result, "json")
        self.mock_authentication_service.login.assert_called_with("username", "password")
        self.mock_jsonify.assert_called_with({"success": True})
