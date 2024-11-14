import pytz
from datetime import datetime

from ..db import db


class Transactions(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shipment_address_id = db.Column(
        db.Integer, db.ForeignKey("shipment_addresses.id"), nullable=False
    )
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    rent_details = db.relationship("RentDetails", backref="transactions_rent_details")

    def __repr__(self):
        return "<Transactions %r>" % self.id

    def __init__(self, shipment_address_id):

        self.shipment_address_id = shipment_address_id

    def to_dict(self):
        shipment_details = (
            self.shipment_addresses.to_dict() if self.shipment_addresses else {}
        )

        return {
            "id": self.id,
            "shipment_address_id": self.shipment_address_id,
            "shipment_details": shipment_details,
        }
