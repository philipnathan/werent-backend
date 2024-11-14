import pytz
from datetime import datetime

from ..db import db


class UserCarts(db.Model):
    __tablename__ = "user_carts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return "<UserCarts %r>" % self.id

    def to_dict(self):
        product = self.products.to_dict() if self.products else {}

        if product == {}:
            return {}

        return {
            "user_id": self.user_id,
            "product": product,
            "quantity": self.quantity,
        }
