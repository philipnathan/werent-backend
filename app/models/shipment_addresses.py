import pytz
from datetime import datetime

from ..db import db


class ShipmentAddresses(db.Model):
    __tablename__ = "shipment_addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    receiver_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(14), nullable=False)
    address_line = db.Column(db.Text, nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey("districts.id"), nullable=False)
    rt_rw = db.Column(db.String(7), nullable=False)
    postal_code = db.Column(db.String(5), nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )
    updated_at = db.Column(
        db.DateTime(), nullable=True, onupdate=lambda: datetime.now(pytz.UTC)
    )

    transactions = db.relationship(
        "Transactions", backref="shipment_addresses_transactions"
    )

    def __repr__(self):
        return "<ShipmentAddresses %r>" % self.receiver_name

    def __init__(
        self,
        user_id,
        receiver_name,
        phone_number,
        address_line,
        district_id,
        rt_rw,
        postal_code,
    ):
        self.user_id = user_id
        self.receiver_name = receiver_name
        self.phone_number = phone_number
        self.address_line = address_line
        self.district_id = district_id
        self.rt_rw = rt_rw
        self.postal_code = postal_code

    def to_dict(self):
        return {
            "id": self.id,
            "receiver_name": self.receiver_name,
            "phone_number": self.phone_number,
            "address_line": self.address_line,
            "district_id": self.district_id,
            "rt_rw": self.rt_rw,
            "postal_code": self.postal_code,
        }
