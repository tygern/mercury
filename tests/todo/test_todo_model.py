from mercury.todo.models import Todo
from tests import MercuryTestCase


class TestTodoModel(MercuryTestCase):
    def test_serialize(self):
        todo = Todo(title="hello", description="there")
        todo.id = 17

        self.assertEquals(todo.serialize, {
            'id': 17,
            'title': 'hello',
            'description': 'there'
        })