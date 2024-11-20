from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request
from flasgger import swag_from

from .reviews_service import ReviewService
from . import reviews_blueprint

service = ReviewService()


@reviews_blueprint.route("/reviews", methods=["GET"])
def get_reviews():
    return service.get_reviews()


@reviews_blueprint.route("/products/<int:product_id>/reviews", methods=["GET"])
@swag_from("./get_all_product_review.yml")
def get_product_reviews(product_id):
    return service.get_product_reviews(product_id=product_id)


@reviews_blueprint.route("/products/<int:product_id>/reviews", methods=["POST"])
@jwt_required()
@swag_from("./create_review.yml")
def add_product_review(product_id):
    identity = get_jwt_identity()
    user_id = int(identity)
    form = request.form
    medias = request.files.getlist("media")
    return service.add_review(
        product_id=product_id, user_id=user_id, form=form, medias=medias
    )


@reviews_blueprint.route("/reviews/<string:review_id>", methods=["POST"])
@jwt_required()
@swag_from("./add_like.yml")
def add_likes(review_id):
    identity = get_jwt_identity()
    user_id = int(identity)
    return service.add_likes(review_id=review_id, user_id=user_id)
