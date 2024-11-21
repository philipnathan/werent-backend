from .products_repository import ProductRepository
from app.db import db
from app.models import Stores


class ProductService:
    def __init__(self, product_repository=ProductRepository, db=db, store=Stores):
        self.product_repository = product_repository()
        self.db = db
        self.store = Stores

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

    def create_product(self, req):
        try:
            properties = ["name", "store_id", "description", "fit", "fabric"]
            data = {}

            for prop in properties:
                if req.get(prop) is None:
                    raise ValueError(f"{prop} is required")

                data[prop] = req.get(prop)

            if self.store.query.get(data["store_id"]) is None:
                raise ValueError("Store not found")

            product = self.product_repository.create_product(data)

            db.session.add(product)
            db.session.commit()

            return {
                "message": "Product created successfully",
                "product_id": product.id,
            }, 201

        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500
