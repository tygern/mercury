class CrudService:
    def __init__(self, model_class, db_session):
        self.db_session = db_session
        self.model_class = model_class

    def find_all(self):
        return self.model_class.query.all()

    def find_by(self, **kwargs):
        return self.model_class.query.filter_by(**kwargs).first()

    def create(self, **kwargs):
        todo = self.model_class(**kwargs)
        self.db_session.add(todo)
        self.db_session.commit()

        return todo
