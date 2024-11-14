import pytz
import bcrypt
from datetime import datetime

from ..db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    phone_number = db.Column(db.String(14), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )
    updated_at = db.Column(
        db.DateTime(), nullable=True, onupdate=lambda: datetime.now(pytz.UTC)
    )

    stores = db.relationship("Stores", backref="users_stores")
    shipment_addresses = db.relationship(
        "ShipmentAddresses", backref="users_shipment_addresses"
    )

    def __repr__(self):
        return "<User %r>" % self.username

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = self.set_password(password)

    def set_password(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def set_to_inactive(self):
        self.is_active = False

    def to_dict(self):
        stores = self.users_stores.to_dict() if self.user_stores else {}

        return {"email": self.email, "username": self.username, "stores": stores}
