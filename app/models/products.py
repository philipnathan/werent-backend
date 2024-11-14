import pytz
import slugify
from datetime import datetime

from ..db import db


class Products(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )
    updated_at = db.Column(
        db.DateTime(), nullable=True, onupdate=lambda: datetime.now(pytz.UTC)
    )

    def __repr__(self):
        return "<Products %r>" % self.name

    def __init__(self, name, store_id, description):
        self.store_id = store_id
        self.name = name
        self.slug = slugify(name)
        self.description = description

    def set_to_inactive(self):
        self.is_active = False

    def set_to_active(self):
        self.is_active = True

    def to_dict(self):
        store = self.stores.to_dict() if self.stores else {}

        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "description": self.description,
            "is_active": self.is_active,
            "store": store,
        }