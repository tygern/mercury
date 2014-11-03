from mock import patch
from mercury.authentication.views import login, logout
from tests import MercuryTestCase


class TestAuthenticationViews(MercuryTestCase):
    def setUp(self):
        self.render_template_patcher = patch('mercury.authentication.views.render_template')
        self.mock_render_template = self.render_template_patcher.start()
        
        self.redirect_patcher = patch('mercury.authentication.views.redirect')
        self.mock_redirect = self.redirect_patcher.start()
        self.mock_redirect.return_value = 'redirect'
        
        self.authentication_service_patcher = patch('mercury.authentication.views.authentication_service')
        self.mock_authentication_service = self.authentication_service_patcher.start()
        
        self.flash_patcher = patch('mercury.authentication.views.flash')
        self.mock_flash = self.flash_patcher.start()
        
        self.oid_patcher = patch('mercury.authentication.views.oid')
        self.mock_oid = self.oid_patcher.start()

        self.mock_oid.get_next_url.return_value = 'next'
        self.mock_oid.fetch_error.return_value = 'error'


    def tearDown(self):
        self.render_template_patcher.stop()
        self.redirect_patcher.stop()
        self.authentication_service_patcher.stop()
        self.oid_patcher.stop()

    def test_logout(self):
        result = logout()

        self.assertEquals(result, "redirect")
        self.mock_authentication_service.logout.assert_called()
        self.mock_redirect.assert_called_with('next')

    @patch('flask_openid.request')
    def test_login_logged_in(self, request):
        self.mock_authentication_service.logged_in.return_value = True
        result = login()

        self.assertEquals(result, "redirect")
        self.mock_redirect.assert_called_with('next')

    @patch('flask_openid.request')
    def test_login_logged_out_post(self, request):
        self.mock_authentication_service.logged_in.return_value = True
        request.method = 'POST'
        result = login()

        self.assertEquals(result, "redirect")
        self.mock_redirect.assert_called_with('next')
