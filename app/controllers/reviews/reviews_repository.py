from app.db import db
from app.models import Reviews, ReviewMedias


class ReviewRepository:
    def __init__(self, review=Reviews, review_media=ReviewMedias, db=db):
        self.review = review
        self.review_media = review_media
        self.db = db

    def create_review(self, review_data):
        return self.review(**review_data)

    def create_review_media(self, media_data):
        return self.review_media(**media_data)

    def get_reviews(self, product_id):
        return self.review.query.filter_by(product_id=product_id).all()
