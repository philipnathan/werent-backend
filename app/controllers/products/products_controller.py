from .products_service import ProductService
from . import products_blueprint

service = ProductService()


@products_blueprint.route("/products", methods=["GET"])
def get_products():
    return service.get_products()


@products_blueprint.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    return service.get_product(product_id)


@products_blueprint.route("/products", methods=["POST"])
def create_product():
    pass
