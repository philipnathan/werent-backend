import pytz
from datetime import datetime

from ..db import db


class ReviewLikes(db.Model):
    __tablename__ = "review_likes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    review_id = db.Column(db.String(36), db.ForeignKey("reviews.id"), nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    def __init__(self, user_id, review_id):
        self.user_id = user_id
        self.review_id = review_id
