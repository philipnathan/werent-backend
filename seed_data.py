from app.db import db
from run import app
from app.models import Districts, Users, Stores, Products, VariantOptions, VariantMedias


def seed_districts():
    try:
        if Districts.query.first():
            print("District data already seeded")
            return

        districts = {
            "id": 1,
            "province_id": 1,
            "province_name": "Bali",
            "district_name": "Denpasar",
        }

        db.session.add(Districts(**districts))
        db.session.commit()

        print("Seeded districts")
    except Exception as e:
        db.session.rollback()
        print(e)


def seed_users():

    try:
        if Users.query.first():
            print("User data already seeded")
            return

        user = {
            "email": "admin@werent.com",
            "username": "admin",
            "password": "admin",
            "phone_number": "081234567890",
            "image_url": "https://milestone-1-s3-bucket.s3.ap-southeast-3.amazonaws.com/admin_image.png",
        }

        db.session.add(Users(**user))
        db.session.commit()

        print("Seeded users")

    except Exception as e:
        db.session.rollback()
        print(e)


def seed_stores():
    try:
        if Stores.query.first():
            print("Store data already seeded")
            return

        user = Users.query.first()
        user_id = user.id

        district = Districts.query.first()
        district_id = district.id

        store = {
            "name": "Milestone 1",
            "store_address": "Jl. Jend. Sudirman No. 1",
            "image_url": "https://milestone-1-s3-bucket.s3.ap-southeast-3.amazonaws.com/store-image.png",
            "user_id": user_id,
            "district_id": district_id,
        }

        db.session.add(Stores(**store))
        db.session.commit()

        print("Seeded stores")

    except Exception as e:
        db.session.rollback()
        print(e)


def seed_products():
    try:
        if Products.query.first():
            print("Product data already seeded")
            return

        store = Stores.query.first()
        store_id = store.id

        product = {
            "store_id": store_id,
            "name": "T-Shirt",
            "description": "T-Shirt description",
            "fit": "Slim",
            "fabric": "Cotton",
        }

        db.session.add(Products(**product))
        db.session.commit()

        print("Seeded products")

    except Exception as e:
        db.session.rollback()
        print(e)


def seed_products_variant_options():
    try:
        if VariantOptions.query.first():
            print("Product variant data already seeded")
            return

        product = Products.query.first()
        product_id = product.id

        variant_product_1 = {
            "product_id": product_id,
            "variant_name": "S",
            "total_stock": 10,
            "price": 10000,
            "bust": 90,
            "length": 100,
        }

        variant_product_2 = {
            "product_id": product_id,
            "variant_name": "M",
            "total_stock": 10,
            "price": 10000,
            "bust": 90,
            "length": 100,
        }

        variant_product_3 = {
            "product_id": product_id,
            "variant_name": "L",
            "total_stock": 10,
            "price": 10000,
            "bust": 90,
            "length": 100,
        }

        db.session.add(VariantOptions(**variant_product_1))
        db.session.add(VariantOptions(**variant_product_2))
        db.session.add(VariantOptions(**variant_product_3))
        db.session.commit()

        print("Seeded products variant options")

    except Exception as e:
        db.session.rollback()
        print(e)


def seed_variant_medias():
    try:
        if VariantMedias.query.first():
            print("Product variant media data already seeded")
            return

        variant_option_1 = VariantOptions.query.filter_by(variant_name="S").first()
        variant_option_1_id = variant_option_1.id

        variant_option_2 = VariantOptions.query.filter_by(variant_name="M").first()
        variant_option_2_id = variant_option_2.id

        variant_option_3 = VariantOptions.query.filter_by(variant_name="L").first()
        variant_option_3_id = variant_option_3.id

        variant_media_1 = {
            "variant_option_id": variant_option_1_id,
            "url": "https://milestone-1-s3-bucket.s3.ap-southeast-3.amazonaws.com/s-3.png",
            "format_item": "image/png",
            "position": 0,
        }

        variant_media_2 = {
            "variant_option_id": variant_option_2_id,
            "url": "https://milestone-1-s3-bucket.s3.ap-southeast-3.amazonaws.com/s-2.png",
            "format_item": "image/png",
            "position": 0,
        }

        variant_media_3 = {
            "variant_option_id": variant_option_3_id,
            "url": "https://milestone-1-s3-bucket.s3.ap-southeast-3.amazonaws.com/s-image.png",
            "format_item": "image/png",
            "position": 0,
        }

        db.session.add(VariantMedias(**variant_media_1))
        db.session.add(VariantMedias(**variant_media_2))
        db.session.add(VariantMedias(**variant_media_3))
        db.session.commit()

        print("Seeded variant medias")

    except Exception as e:
        db.session.rollback()
        print(e)


if __name__ == "__main__":
    with app.app_context():
        try:
            seed_districts()
            seed_users()
            seed_stores()
            seed_products()
            seed_products_variant_options()
            seed_variant_medias()

            print("Seeded data successfully")
        except Exception as e:
            print("Failed to seed data: ", str(e))
