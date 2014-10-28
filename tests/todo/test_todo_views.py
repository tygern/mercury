from werkzeug.exceptions import Unauthorized
from mercury.todo.views import show_todos, add_todo

from mock import patch, MagicMock
from mercury.todo.models import Todo
from tests import MercuryTestCase


class TestTodoViews(MercuryTestCase):

    def setUp(self):
        self.todo_service_patcher = patch('mercury.todo.views.todo_service')
        self.mock_todo_service = self.todo_service_patcher.start()

    def tearDown(self):
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
    @patch('mercury.todo.views.session')
    @patch('mercury.todo.views.serialize')
    def test_add_todo(self, mock_serialize, mock_session, mock_request):
        self.mock_todo_service.create.return_value = Todo('test', 'todo')
        mock_serialize.return_value = 'todo'
        mock_session.get = MagicMock(return_value=True)
        mock_request.form = {"title": "new todo", "description": "really cool"}

        result = add_todo()

        self.assertEquals(result, 'todo')
        self.mock_todo_service.create.assert_called_with("new todo", "really cool")

    @patch('mercury.todo.views.session')
    def test_add_todo_logged_out(self, mock_session):
        mock_session.get = MagicMock(return_value=False)

        self.assertRaises(Unauthorized, add_todo)
        mock_session.get.assert_called_with('logged_in')
