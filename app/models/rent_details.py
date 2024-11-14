import pytz
from datetime import datetime

from ..db import db


class RentDetails(db.Model):
    __tablename__ = "rent_details"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction_id = db.Column(
        db.Integer, db.ForeignKey("transactions.id"), nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    variant_option_id = db.Column(
        db.Integer, db.ForeignKey("variant_options.id"), nullable=False
    )
    quantity = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    def __repr__(self):
        return "<RentDetails %r>" % self.id

    def __init__(
        self, transaction_id, user_id, variant_option_id, quantity, start_date, end_date
    ):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.variant_option_id = variant_option_id
        self.quantity = quantity
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self):
        return {
            "id": self.id,
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "variant_option_id": self.variant_option_id,
            "quantity": self.quantity,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
