import random
from data import mockProducts

from app.db import db
from run import app
from app.models import (
    Districts,
    Users,
    Stores,
    Products,
    VariantOptions,
    VariantMedias,
    Reviews,
)


def seed_districts():
    try:
        if Districts.query.first():
            print("District data already seeded")
            return

        districts = [
            {
                "id": 1,
                "province_id": 1,
                "province_name": "Bali",
                "district_name": "Denpasar",
            },
            {
                "id": 2,
                "province_id": 2,
                "province_name": "Jawa Barat",
                "district_name": "Bandung",
            },
            {
                "id": 3,
                "province_id": 3,
                "province_name": "Jawa Tengah",
                "district_name": "Surabaya",
            },
        ]

        for dis in districts:
            db.session.add(Districts(**dis))
        db.session.commit()

        print("Seeded districts")
    except Exception as e:
        db.session.rollback()
        print(e)


def seeding(eq):
    try:
        designer_without_space_and_lowercase = (
            eq["designer_name"].replace(" ", "").lower()
        )
        d = designer_without_space_and_lowercase
        position = 0

        new_user = Users(
            username=f"{eq['designer_name']}{random.randrange(1, 10000)}",
            email=f"{d}@{d}{random_10_digit()}.com",
            password=f"{d}",
            image_url=eq.get("image_designer"),
            phone_number=random_10_digit(),
        )

        db.session.add(new_user)
        db.session.commit()
        print("success add user")

        new_store = Stores(
            name=f"{eq["designer_name"]}.{random.randrange(1, 10000)}",
            store_address=eq["designer_name"],
            image_url=eq.get("image_designer"),
            user_id=new_user.id,
            district_id=random.randrange(1, 3),
        )

        db.session.add(new_store)
        db.session.commit()
        print("success add store")

        new_product = Products(
            name=eq.get("title"),
            store_id=new_store.id,
            description=eq.get("title"),
            fit=eq.get("fit", "Slim Fit"),
            fabric=eq.get("fabric", "Cotton"),
        )

        db.session.add(new_product)
        db.session.commit()
        print("success add product")

        new_variant = VariantOptions(
            product_id=new_product.id,
            variant_name=(
                eq.get("dimensions", None).get("size", None)
                if eq.get("dimensions")
                else "S"
            ),
            total_stock=random.randrange(1, 10),
            price=random.randrange(15000, 2000000, 5000),
            bust=(
                int(eq.get("dimensions", None).get("waist", None))
                if eq.get("dimensions")
                else 50
            ),
            length=(
                int(eq.get("dimensions", None).get("length", None))
                if eq.get("dimensions")
                else 100
            ),
        )

        db.session.add(new_variant)
        db.session.commit()
        print("success add variant")

        new_media = []
        if isinstance(eq.get("images"), list):
            for img in eq["images"]:
                var_med = VariantMedias(
                    variant_option_id=new_variant.id,
                    url=(
                        img
                        if img
                        else "https://images.pexels.com/photos/3765550/pexels-photo-3765550.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
                    ),
                    format_item="image/jpg",
                    position=position,
                )
                new_media.append(var_med)
                position += 1

        else:
            var_med = VariantMedias(
                variant_option_id=new_variant.id,
                url=eq.get(
                    "images",
                    "https://images.pexels.com/photos/3765550/pexels-photo-3765550.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                ),
                format_item="image/jpg",
                position=position,
            )
            new_media.append(var_med)

        db.session.add_all(new_media)
        db.session.commit()
        print("success add media")

        reviews = []
        for review in eq["review"]:
            reviewer = Users(
                username=f"{review['user_name']}{random.randrange(1, 10000)}",
                email=f"{review['user_name']}@{review['user_name']}{random_10_digit()}.com",
                password=f"{review['user_name'].replace(' ', '').lower()}",
                image_url=review["user_avatar"],
                phone_number=random_10_digit(),
            )

            db.session.add(reviewer)
            db.session.commit()

            new_review = Reviews(
                user_id=reviewer.id,
                product_id=new_product.id,
                rating=review["rating"],
                comment=review["comment"],
                id=random_10_digit(),
            )

            reviews.append(new_review)

        db.session.add_all(reviews)
        db.session.commit()

        print("success add review")
    except Exception as e:
        db.session.rollback()
        print(e)


def random_10_digit():
    return "".join(str(random.randint(0, 9)) for _ in range(10))


if __name__ == "__main__":
    with app.app_context():
        try:
            seed_districts()
            for eq in mockProducts:
                seeding(eq)

            print("Seeded data successfully")
        except Exception as e:
            print("Failed to seed data: ", str(e))
