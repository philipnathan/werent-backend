import pytz
from datetime import datetime

from ..db import db


class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now(pytz.UTC)
    )

    review_likes = db.relationship(
        "ReviewLikes",
        backref="reviews_review_likes",
    )
    review_medias = db.relationship(
        "ReviewMedias",
        backref="reviews_review_medias",
    )

    @property
    def like_count(self):
        return len(self.review_likes)

    @property
    def media_list(self):
        return [media.to_dict() for media in self.review_medias]

    def __init__(self, user_id, product_id, rating, comment):
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating
        self.comment = comment

    def to_dict(self):
        user = self.users.to_dict() if self.users else {}

        return {
            "id": self.id,
            "user": user,
            "product_id": self.product_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at,
            "like_count": self.like_count,
            "review_medias": self.media_list,
        }
