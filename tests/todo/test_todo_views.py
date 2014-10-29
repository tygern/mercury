from werkzeug.exceptions import Unauthorized
from mercury.todo.views import show_todos, add_todo

from mock import patch
from mercury.todo.models import Todo
from tests import MercuryTestCase


class TestTodoViews(MercuryTestCase):

    def setUp(self):
        self.todo_service_patcher = patch('mercury.todo.views.todo_service')
        self.mock_todo_service = self.todo_service_patcher.start()

        self.authentication_service_patcher = patch('mercury.todo.views.authentication_service')
        self.mock_authentication_service = self.authentication_service_patcher.start()
        attrs = {"logged_in.return_value": True}
        self.mock_authentication_service.configure_mock(**attrs)

    def tearDown(self):
        self.authentication_service_patcher.stop()
        self.todo_service_patcher.stop()

    @patch('mercury.todo.views.serialize_list')
    def test_show_todos(self, mock_serialize_list):
        todos = [Todo('test', 'todo')]
        self.mock_todo_service.find_all.return_value = todos
        mock_serialize_list.return_value = ['todo']

        result = show_todos()

        mock_serialize_list.assert_called_with('todos', todos)
        self.assertEquals(result, ['todo'])

    @patch('mercury.todo.views.request')
    @patch('mercury.todo.views.serialize')
    def test_add_todo(self, mock_serialize, mock_request):
        self.mock_todo_service.create.return_value = Todo('test', 'todo')

        mock_serialize.return_value = 'todo'
        mock_request.form = {"title": "new todo", "description": "really cool"}

        result = add_todo()

        self.assertEquals(result, 'todo')
        self.mock_todo_service.create.assert_called_with(title="new todo", description="really cool")

    def test_add_todo_logged_out(self):
        attrs = {"logged_in.return_value": False}
        self.mock_authentication_service.configure_mock(**attrs)

        self.assertRaises(Unauthorized, add_todo)