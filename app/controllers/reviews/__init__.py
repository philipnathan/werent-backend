from flask import Blueprint

reviews_blueprint = Blueprint("reviews", __name__, url_prefix="/api/v1/")

from . import reviews_controller
