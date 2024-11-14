import pytz
from datetime import datetime

from ..db import db


class Districts(db.Model):
    __tablename__ = "districts"

    id = db.Column(db.Integer, primary_key=True)
    province_id = db.Column(db.Integer, nullable=False)
    province_name = db.Column(db.String(255), nullable=False)
    district_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    stores = db.relationship("Stores", backref="districts_stores")
    shipment_addresses = db.relationship(
        "ShipmentAddresses", backref="districts_shipment_addresses"
    )

    def __repr__(self):
        return "<Districts %r>" % self.district_name

    def __init__(self, id, province_id, province_name, district_name):
        self.id = id
        self.province_id = province_id
        self.province_name = province_name
        self.district_name = district_name

    def to_dict(self):
        return {
            "id": self.id,
            "province_id": self.province_id,
            "province_name": self.province_name,
            "district_name": self.district_name,
        }
