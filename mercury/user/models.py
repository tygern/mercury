from mercury import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    openid = db.Column(db.String(), index=True)

    def __init__(self, name, email, openid):
        self.name = name
        self.email = email
        self.openid = openid

    def __repr__(self):
        return '<id {}>'.format(self.id)