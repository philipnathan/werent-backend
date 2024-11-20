import pytz
from datetime import datetime

from ..db import db


class VariantMedias(db.Model):
    __tablename__ = "variant_medias"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    variant_option_id = db.Column(
        db.Integer, db.ForeignKey("variant_options.id"), nullable=False
    )
    url = db.Column(db.Text, nullable=False)
    format_item = db.Column(db.String(50), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    def __init__(self, variant_option_id, url, format_item, position):
        self.variant_option_id = variant_option_id
        self.url = url
        self.format_item = format_item
        self.position = position

    def to_dict(self):
        return {
            "id": self.id,
            "variant_option_id": self.variant_option_id,
            "url": self.url,
            "format": self.format,
            "position": self.position,
        }
