from mock import MagicMock
from mercury.services import CrudService
from tests import MercuryTestCase


class TestCrudService(MercuryTestCase):

    def test_find_all(self):
        object_collection = ['object']
        crud_class = MagicMock()
        crud_class.query.all.return_value = object_collection
        service = CrudService(crud_class, None)

        result = service.find_all()

        self.assertEquals(result, object_collection)

    def test_find_by(self):
        single_object = 'object'
        crud_class = MagicMock()

        query_result = MagicMock()
        query_result.first.return_value = single_object

        crud_class.query.filter_by.return_value = query_result

        service = CrudService(crud_class, None)
        result = service.find_by(any="arguments", go="here")

        crud_class.query.filter_by.assert_called_with(any="arguments", go="here")
        self.assertEquals(result, single_object)

    def test_create(self):
        single_object = 'object'
        crud_class = MagicMock(return_value=single_object)

        db_session = MagicMock()
        db_session.add = MagicMock()
        db_session.commit = MagicMock()

        service = CrudService(crud_class, db_session)

        result = service.create(any='arguments', will='work')

        self.assertEquals(result, single_object)
        crud_class.assert_called_with(any='arguments', will='work')
        db_session.add.assert_called_with(single_object)