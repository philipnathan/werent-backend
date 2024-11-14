import pytz
from datetime import datetime

from ..db import db


class Stores(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    store_address = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )
    updated_at = db.Column(
        db.DateTime(), nullable=True, onupdate=lambda: datetime.now(pytz.UTC)
    )

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return "<Stores %r>" % self.name

    def __init__(self, name, store_address, user_id):
        self.name = name
        self.store_address = store_address
        self.user_id = user_id

    def to_dict(self):
        return {"id": self.id, "name": self.name, "store_address": self.store_address}

    def set_to_inactive(self):
        self.is_active = False

    def set_to_active(self):
        self.is_active = True
