from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

meta = MetaData(schema='clients')
db = SQLAlchemy(metadata=meta)


class Client(db.Model):
    __tablename__ = 'tt_clients'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    dob = db.Column(db.Date)
    social_status_id = db.Column(db.Integer)
    gender = db.Column(db.String(1))

    def __repr__(self):
        return '<Client %r>' % self.id


class Dictionary(db.Model):
    __tablename__ = 'tt_dictionary'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(25))
    str_id = db.Column(db.String(50))
    int_id = db.Column(db.Integer)
    value = db.Column(db.String(255))

    def __repr__(self):
        return '<Disctionary %r>' % self.id
