from ..db import db


class UserWishlists(db.Model):
    __tablename__ = "user_wishlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

    def to_dict(self):
        product = self.products.to_dict() if self.products else {}

        return {
            "user_id": self.user_id,
            "product": product,
        }
