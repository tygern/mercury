class Session():
    def __init__(self, db):
        self.session = db.session

    def __enter__(self):
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.commit()