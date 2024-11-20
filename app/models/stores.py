import pytz
import slugify
from datetime import datetime

from ..db import db


class Stores(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    slug = db.Column(db.String(30), nullable=False, unique=True)
    store_address = db.Column(db.Text, nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey("districts.id"), nullable=False)
    image_url = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )
    updated_at = db.Column(
        db.DateTime(), nullable=True, onupdate=lambda: datetime.now(pytz.UTC)
    )

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    products = db.relationship("Products", backref="stores_products")

    def __repr__(self):
        return "<Stores %r>" % self.name

    def __init__(self, name, store_address, user_id, district_id, image_url):
        self.name = name
        self.slug = slugify.slugify(name)
        self.store_address = store_address
        self.user_id = user_id
        self.district_id = district_id
        self.image_url = image_url

    def to_dict(self):
        district = self.districts_stores.to_dict() if self.districts_stores else {}

        return {
            "id": self.id,
            "name": self.name,
            "store_address": self.store_address,
            "image_url": self.image_url,
            "district": district,
        }

    def set_to_inactive(self):
        self.is_active = False

    def set_to_active(self):
        self.is_active = True
