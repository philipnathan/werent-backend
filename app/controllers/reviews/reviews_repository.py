from app.db import db
from app.models import Reviews, ReviewMedias, ReviewLikes


class ReviewRepository:
    def __init__(
        self, review=Reviews, review_media=ReviewMedias, db=db, review_like=ReviewLikes
    ):
        self.review = review
        self.review_media = review_media
        self.db = db
        self.review_like = review_like

    def create_review(self, review_data):
        return self.review(**review_data)

    def create_review_media(self, media_data):
        return self.review_media(**media_data)

    def get_reviews(self, product_id):
        return self.review.query.filter_by(product_id=product_id).all()

    def get_review_by_id(self, review_id):
        return self.review.query.filter_by(id=review_id).first()

    def get_review_like_by_user_id(self, user_id, review_id):
        return self.review_like.query.filter_by(
            user_id=user_id, review_id=review_id
        ).first()

    def create_review_like(self, user_id, review_id):
        return self.review_like(user_id=user_id, review_id=review_id)
