from flasgger import swag_from
from flask import request

from .products_service import ProductService
from .variant_options_service import VariantOptionsService
from . import products_blueprint

service = ProductService()
variant_service = VariantOptionsService()


@products_blueprint.route("/products", methods=["GET"])
@swag_from("./get_all_products.yml")
def get_products():
    return service.get_products()


@products_blueprint.route("/products/<int:product_id>", methods=["GET"])
@swag_from("./get_detail_product.yml")
def get_product(product_id):
    return service.get_product(product_id)


@products_blueprint.route("/products", methods=["POST"])
@swag_from("./create_product.yml")
def create_product():
    req = request.get_json()
    return service.create_product(req=req)


@products_blueprint.route(
    "/products/<int:product_id>/variant_options", methods=["POST"]
)
@swag_from("./create_variant_options.yml")
def create_variant_option(product_id):
    form = request.form
    return variant_service.create_variant_option(product_id=product_id, form=form)
