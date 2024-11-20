from flask import Blueprint

products_blueprint = Blueprint("products", __name__, url_prefix="/api/v1/")

from . import products_controller
