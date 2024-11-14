import pytz
from datetime import datetime
from enum import Enum

from ..db import db


class MediaFormat(Enum):
    IMAGE = "image"
    VIDEO = "video"


class ReviewMedias(db.Model):
    __tablename__ = "review_medias"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.id"), nullable=False)
    url = db.Column(db.Text, nullable=False)
    format = db.Column(db.Enum(MediaFormat), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    def __init__(self, review_id, url, format, position):
        self.review_id = review_id
        self.url = url
        self.format = format
        self.position = position

    def to_dict(self):
        return {
            "id": self.id,
            "review_id": self.review_id,
            "url": self.url,
            "format": self.format,
            "position": self.position,
        }
