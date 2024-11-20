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
    fit = db.Column(db.String(20), nullable=False)
    fabric = db.Column(db.String(20), nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )
    updated_at = db.Column(
        db.DateTime(), nullable=True, onupdate=lambda: datetime.now(pytz.UTC)
    )

    variant_options = db.relationship(
        "VariantOptions", backref="products_variant_options"
    )
    reviews = db.relationship("Reviews", backref="products_reviews")

    def __repr__(self):
        return "<Products %r>" % self.name

    def __init__(self, name, store_id, description, fit, fabric):
        self.store_id = store_id
        self.name = name
        self.slug = slugify.slugify(name)
        self.description = description
        self.fit = fit
        self.fabric = fabric

    def set_to_inactive(self):
        self.is_active = False

    def set_to_active(self):
        self.is_active = True

    def to_dict(self):
        store = self.stores_products.to_dict() if self.stores_products else {}
        variant_options = [option.to_dict() for option in self.variant_options]
        first_price = variant_options[0]["price"]
        reviews = [review.to_dict() for review in self.reviews]
        total_reviews = len(reviews) if reviews else 0
        average_rating = (
            sum([review["rating"] for review in reviews]) / total_reviews
            if total_reviews > 0
            else 0
        )

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active,
            "store": store,
            "variant_options": variant_options,
            "price": first_price,
            "reviews": reviews,
            "fit": self.fit,
            "fabric": self.fabric,
            "total_reviews": total_reviews,
            "average_rating": average_rating,
        }
