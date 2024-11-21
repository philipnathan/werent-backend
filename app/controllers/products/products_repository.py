from app.db import db
from app.models import Products


class ProductRepository:
    def __init__(self, product=Products, db=db):
        self.product = product
        self.db = db

    def get_products(self):
        products = self.product.query.all()
        return products

    def get_product(self, product_id):
        product = self.product.query.get(product_id)
        return product

    def create_product(self, data):
        product = self.product(**data)
        return product
