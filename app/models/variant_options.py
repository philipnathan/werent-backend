import pytz
from datetime import datetime

from ..db import db


class VariantOptions(db.Model):
    __tablename__ = "variant_options"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    variant_name = db.Column(db.String(20), nullable=False)
    total_stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    bust = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )
    updated_at = db.Column(
        db.DateTime(), nullable=True, onupdate=lambda: datetime.now(pytz.UTC)
    )

    variant_medias = db.relationship(
        "VariantMedias", backref="variant_options_variant_medias"
    )

    rent_details = db.relationship(
        "RentDetails", backref="rent_details_variant_options"
    )

    def __init__(self, product_id, variant_name, total_stock, price):
        self.product_id = product_id
        self.variant_name = variant_name
        self.total_stock = total_stock
        self.price = price

    def __repr__(self):
        return "<VariantOptions %r>" % self.id

    def to_dict(self):
        variant_medias = [
            variant_media.to_dict() for variant_media in self.variant_medias
        ]

        return {
            "id": self.id,
            "product_id": self.product_id,
            "variant_name": self.variant_name,
            "variant_medias": variant_medias,
            "total_stock": self.total_stock,
            "price": self.price,
            "bust": self.bust,
            "length": self.length,
        }

    # TODO
    # buat available_stock untuk to_dict() -> harus didapatkan dari total_stock - rent_details (entity)
