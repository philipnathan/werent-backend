from .products_repository import ProductRepository
from app.db import db


class ProductService:
    def __init__(self, product_repository=ProductRepository, db=db):
        self.product_repository = product_repository()
        self.db = db

    def get_products(self):
        products = self.product_repository.get_products()
        products_dict = [product.to_dict() for product in products]
        return [
            {
                "id": product["id"],
                "name": product["name"],
                "is_active": product["is_active"],
                "store_name": product["store"]["name"],
                "price": product["price"],
                "total_reviews": product["total_reviews"],
                "average_rating": product["average_rating"],
                "image_url": product["variant_options"][0]["variant_medias"][0]["url"],
            }
            for product in products_dict
        ]

    def get_product(self, product_id):
        product = self.product_repository.get_product(product_id)
        return product.to_dict()
