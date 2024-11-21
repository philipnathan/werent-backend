import pytz
from datetime import datetime

from ..db import db


class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    rating = db.Column(db.Float, nullable=False)
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

    review_users = db.relationship(
        "Users",
        backref="reviews_review_users",
    )

    @property
    def like_count(self):
        return len(self.review_likes)

    @property
    def media_list(self):
        return [media.to_dict() for media in self.review_medias]

    def __init__(self, user_id, product_id, rating, comment, id):
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating
        self.comment = comment
        self.id = id

    def to_dict(self):
        user = self.review_users.to_dict() if self.review_users else {}

        return {
            "id": self.id,
            "user": {
                "username": user.get("username"),
                "image_url": user.get("image_url"),
            },
            "product_id": self.product_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at,
            "like_count": self.like_count,
            "review_medias": self.media_list,
        }
