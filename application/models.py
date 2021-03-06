from . import db


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        nullable=False
    )
