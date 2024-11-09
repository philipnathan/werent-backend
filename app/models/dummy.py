from ..db import db


class Dummy(db.Model):
    __tablename__ = "dummy"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
