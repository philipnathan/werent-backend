import pytz
from datetime import datetime

from ..db import db


class ReviewMedias(db.Model):
    __tablename__ = "review_medias"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review_id = db.Column(db.String(36), db.ForeignKey("reviews.id"), nullable=False)
    url = db.Column(db.Text, nullable=False)
    format_media = db.Column(db.String(50), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    def __init__(self, review_id, url, format_media, position):
        self.review_id = review_id
        self.url = url
        self.format_media = format_media
        self.position = position

    def to_dict(self):
        return {
            "id": self.id,
            "review_id": self.review_id,
            "url": self.url,
            "format_media": self.format_media,
            "position": self.position,
        }
