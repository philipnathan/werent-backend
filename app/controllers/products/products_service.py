from .products_repository import ProductRepository
from app.db import db
from app.utils import S3Helper


class ProductService:
    def __init__(self, product_repository=ProductRepository, db=db):
        self.product_repository = product_repository()
        self.db = db

    def get_products(self):
        products = self.product_repository.get_products()
        return [product.to_dict() for product in products]

    def get_product(self, product_id):
        product = self.product_repository.get_product(product_id)
        return product.to_dict()
