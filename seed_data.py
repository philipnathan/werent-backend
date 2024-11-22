from app.db import db
from run import app
from app.models import Districts, Users, Stores, Products, VariantOptions, VariantMedias


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


def seed_users():

    try:
        if Users.query.first():
            print("User data already seeded")
            return

        user = [
    # User 1
    {
        "email": "john.doe@example.com",
        "username": "johndoe",
        "password": "password123",
        "phone_number": "081234567890",
        "image_url": "https://images.pexels.com/photos/1545590/pexels-photo-1545590.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    },
    # User 2
    {
        "email": "jane.smith@example.com",
        "username": "janesmith",
        "password": "password456",
        "phone_number": "081234567891",
        "image_url": "https://example.com/images/janesmith.png",
    },
    # User 3
    {
        "email": "mark.brown@example.com",
        "username": "markbrown",
        "password": "password789",
        "phone_number": "081234567892",
        "image_url": "https://example.com/images/markbrown.png",
    },
    # User 4
    {
        "email": "lisa.green@example.com",
        "username": "lisagreen",
        "password": "password101",
        "phone_number": "081234567893",
        "image_url": "https://example.com/images/lisagreen.png",
    },
    # User 5
    {
        "email": "emma.white@example.com",
        "username": "emmawhite",
        "password": "password202",
        "phone_number": "081234567894",
        "image_url": "https://example.com/images/emmawhite.png",
    },
    # User 6
    {
        "email": "james.taylor@example.com",
        "username": "jamestaylor",
        "password": "password303",
        "phone_number": "081234567895",
        "image_url": "https://example.com/images/jamestaylor.png",
    },
    # User 7
    {
        "email": "olivia.jones@example.com",
        "username": "oliviajones",
        "password": "password404",
        "phone_number": "081234567896",
        "image_url": "https://example.com/images/oliviajones.png",
    },
    # User 8
    {
        "email": "william.lee@example.com",
        "username": "williamlee",
        "password": "password505",
        "phone_number": "081234567897",
        "image_url": "https://example.com/images/williamlee.png",
    },
    # User 9
    {
        "email": "sophia.moore@example.com",
        "username": "sophiamoore",
        "password": "password606",
        "phone_number": "081234567898",
        "image_url": "https://example.com/images/sophiamoore.png",
    },
    # User 10
    {
        "email": "logan.thomas@example.com",
        "username": "loganthomas",
        "password": "password707",
        "phone_number": "081234567899",
        "image_url": "https://example.com/images/loganthomas.png",
    },
    # User 11
    {
        "email": "mia.davis@example.com",
        "username": "miadavis",
        "password": "password808",
        "phone_number": "081234567800",
        "image_url": "https://example.com/images/miadavis.png",
    },
    # User 12
    {
        "email": "noah.harris@example.com",
        "username": "noahharris",
        "password": "password909",
        "phone_number": "081234567801",
        "image_url": "https://example.com/images/noahharris.png",
    },
    # User 13
    {
        "email": "ava.martin@example.com",
        "username": "avamartin",
        "password": "password010",
        "phone_number": "081234567802",
        "image_url": "https://example.com/images/avamartin.png",
    },
    # User 14
    {
        "email": "lucas.king@example.com",
        "username": "lucasking",
        "password": "password111",
        "phone_number": "081234567803",
        "image_url": "https://example.com/images/lucasking.png",
    },
    # User 15
    {
        "email": "charlotte.baker@example.com",
        "username": "charlottebaker",
        "password": "password212",
        "phone_number": "081234567804",
        "image_url": "https://example.com/images/charlottebaker.png",
    },
    # User 16
    {
        "email": "henry.wright@example.com",
        "username": "henrywright",
        "password": "password313",
        "phone_number": "081234567805",
        "image_url": "https://example.com/images/henrywright.png",
    },
    # User 17
    {
        "email": "amelia.clark@example.com",
        "username": "ameliaclark",
        "password": "password414",
        "phone_number": "081234567806",
        "image_url": "https://example.com/images/ameliaclark.png",
    },
    # User 18
    {
        "email": "ethan.hall@example.com",
        "username": "ethanhall",
        "password": "password515",
        "phone_number": "081234567807",
        "image_url": "https://example.com/images/ethanhall.png",
    },
    # User 19
    {
        "email": "isabella.allen@example.com",
        "username": "isabellaallen",
        "password": "password616",
        "phone_number": "081234567808",
        "image_url": "https://example.com/images/isabellaallen.png",
    },
    # User 20
    {
        "email": "jackson.young@example.com",
        "username": "jacksonyoung",
        "password": "password717",
        "phone_number": "081234567809",
        "image_url": "https://example.com/images/jacksonyoung.png",
    },
    # User 21
    {
        "email": "harper.scott@example.com",
        "username": "harperscott",
        "password": "password818",
        "phone_number": "081234567810",
        "image_url": "https://example.com/images/harperscott.png",
    },
    # User 22
    {
        "email": "alexander.adams@example.com",
        "username": "alexanderadams",
        "password": "password919",
        "phone_number": "081234567811",
        "image_url": "https://example.com/images/alexanderadams.png",
    },
    # User 23
    {
        "email": "ella.nelson@example.com",
        "username": "ellanelson",
        "password": "password020",
        "phone_number": "081234567812",
        "image_url": "https://example.com/images/ellanelson.png",
    },
    # User 24
    {
        "email": "liam.carter@example.com",
        "username": "liamcarter",
        "password": "password121",
        "phone_number": "081234567813",
        "image_url": "https://example.com/images/liamcarter.png",
    },
]


        for us in user:
            db.session.add(Users(**us))
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

        store = [
            #store1
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 1",
                "image_url": "https://images.pexels.com/photos/1545590/pexels-photo-1545590.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 1,
                "district_id": 1,
            },
            #store2
            {
                "name": "Bobi Santoso",
                "store_address": "Jl. Jend. Sudirman No. 2",
                "image_url": "https://images.pexels.com/photos/7716946/pexels-photo-7716946.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 2,
                "district_id": 2,
            },
            #store3
            {
                "name": "Afina Natalie",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 3,
                "district_id": 3,
            },
            #store4
            {
                "name": "Alvin Makaron",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/1674752/pexels-photo-1674752.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 4,
                "district_id": 3,
            },
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store6
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
            #store5
            {
                "name": "Nadila Airini",
                "store_address": "Jl. Jend. Sudirman No. 3",
                "image_url": "https://images.pexels.com/photos/4556683/pexels-photo-4556683.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "user_id": 5,
                "district_id": 2,
            },
            
        ]

        for st in store:
            db.session.add(Stores(**st))

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

        product = [
            {
            "store_id": store_id,
            "name": "Wedding Dress Zalora",
            "description": "Wedding Dress Zalora",
            "fit": "TRUE TO SIZE",
            "fabric": "SILK",
        },
            {
            "store_id": store_id,
            "name": "Blazzer Zara",
            "description": "Blazzer Zara",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Mini Dress Pink",
            "description": "Mini Dress Pink",
            "fit": "Slim",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Indian Dress",
            "description": "Indian Dress",
            "fit": "Turn on size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Wedding Dress Zalora",
            "description": "Wedding Dress Zalora",
            "fit": "Turn on size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Blazzer Zara",
            "description": "Blazzer Zara",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Mini Dress Pink",
            "description": "Mini Dress Pink",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Indian Dress",
            "description": "Indian Dress",
            "fit": "Turn on size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Wedding Dress Zalora",
            "description": "Wedding Dress Zalora",
            "fit": "Slim",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Blazzer Zara",
            "description": "Blazzer Zara",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Mini Dress Pink",
            "description": "Mini Dress Pink",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Indian Dress",
            "description": "Indian Dress",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Wedding Dress Zalora",
            "description": "Wedding Dress Zalora",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Blazzer Zara",
            "description": "Blazzer Zara",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Mini Dress Pink",
            "description": "Mini Dress Pink",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Indian Dress",
            "description": "Indian Dress",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
        
            {
            "store_id": store_id,
            "name": "Wedding Dress Zalora",
            "description": "Wedding Dress Zalora",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Blazzer Zara",
            "description": "Blazzer Zara",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
        
            {
            "store_id": store_id,
            "name": "Mini Dress Pink",
            "description": "Mini Dress Pink",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
            {
            "store_id": store_id,
            "name": "Indian Dress",
            "description": "Indian Dress",
            "fit": "Turn on Size",
            "fabric": "Cotton",
        },
        
        
        
        ]



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
            "variant_name": "M",
            "total_stock": 10,
            "price": 2030000,
            "bust": 50,
            "length": 15,
        }

        variant_product_2 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 10,
            "price": 750000,
            "bust": 50,
            "length": 15,
        }

        variant_product_3 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 3050000,
            "bust": 50,
            "length": 15,
        }

        variant_product_4 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 670000,
            "bust": 50,
            "length": 15,
        }
        variant_product_5 = {
            "product_id": product_id,
            "variant_name": "30",
            "total_stock": 100,
            "price": 5000000,
            "bust": 50,
            "length": 15,
        }
        variant_product_6 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 750000,
            "bust": 50,
            "length": 15,
        }
        variant_product_7 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 3050000,
            "bust": 50,
            "length": 15,
        }
        variant_product_8 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 670000,
            "bust": 50,
            "length": 15,
        }
        variant_product_9 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 2000000,
            "bust": 50,
            "length": 15,
        }
        variant_product_10 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 750000,
            "bust": 50,
            "length": 15,
        }
        variant_product_11 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 3050000,
            "bust": 50,
            "length": 15,
        }
        variant_product_12 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 670000,
            "bust": 50,
            "length": 15,
        }
        variant_product_13 = {
            "product_id": product_id,
            "variant_name": "30",
            "total_stock": 100,
            "price": 5000000,
            "bust": 40,
            "length": 15,
        }
        variant_product_14 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 750000,
            "bust": 50,
            "length": 15,
        }
        variant_product_15 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 3050000,
            "bust": 50,
            "length": 15,
        }
        variant_product_16 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 670000,
            "bust": 50,
            "length": 15,
        }
        variant_product_17 = {
            "product_id": product_id,
            "variant_name": "30",
            "total_stock": 100,
            "price": 5000000,
            "bust": 40,
            "length": 10,
        }
        variant_product_18 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 750000,
            "bust": 50,
            "length": 15,
        }
        variant_product_19 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 3050000,
            "bust": 50,
            "length": 15,
        }
        variant_product_20 = {
            "product_id": product_id,
            "variant_name": "20",
            "total_stock": 100,
            "price": 670000,
            "bust": 50,
            "length": 15,
        }

        db.session.add(VariantOptions(**variant_product_1))
        db.session.add(VariantOptions(**variant_product_2))
        db.session.add(VariantOptions(**variant_product_3))
        db.session.add(VariantOptions(**variant_product_4))
        db.session.add(VariantOptions(**variant_product_5))
        db.session.add(VariantOptions(**variant_product_6))
        db.session.add(VariantOptions(**variant_product_7))
        db.session.add(VariantOptions(**variant_product_8))
        db.session.add(VariantOptions(**variant_product_9))
        db.session.add(VariantOptions(**variant_product_10))
        db.session.add(VariantOptions(**variant_product_11))
        db.session.add(VariantOptions(**variant_product_12))
        db.session.add(VariantOptions(**variant_product_13))
        db.session.add(VariantOptions(**variant_product_14))
        db.session.add(VariantOptions(**variant_product_15))
        db.session.add(VariantOptions(**variant_product_16))
        db.session.add(VariantOptions(**variant_product_17))
        db.session.add(VariantOptions(**variant_product_18))
        db.session.add(VariantOptions(**variant_product_19))
        db.session.add(VariantOptions(**variant_product_20))
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

        variant_option_1 = VariantOptions.query.filter_by(variant_name="M").first()
        variant_option_1_id = variant_option_1.id

        variant_option_2 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_2_id = variant_option_2.id

        variant_option_3 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_3_id = variant_option_3.id

        variant_option_4 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_4_id = variant_option_4.id


        variant_option_5 = VariantOptions.query.filter_by(variant_name="30").first()
        variant_option_5_id = variant_option_5.id


        variant_option_6 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_6_id = variant_option_6.id


        variant_option_7 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_7_id = variant_option_7.id


        variant_option_8 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_8_id = variant_option_8.id


        variant_option_9 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_9_id = variant_option_9.id


        variant_option_10 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_10_id = variant_option_10.id


        variant_option_11 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_11_id = variant_option_11.id


        variant_option_12 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_12_id = variant_option_12.id


        variant_option_13 = VariantOptions.query.filter_by(variant_name="30").first()
        variant_option_13_id = variant_option_13.id


        variant_option_14 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_14_id = variant_option_14.id


        variant_option_15 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_15_id = variant_option_15.id


        variant_option_16 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_16_id = variant_option_16.id


        variant_option_17 = VariantOptions.query.filter_by(variant_name="30").first()
        variant_option_17_id = variant_option_17.id


        variant_option_18 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_18_id = variant_option_18.id


        variant_option_19 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_19_id = variant_option_19.id


        variant_option_20 = VariantOptions.query.filter_by(variant_name="20").first()
        variant_option_20_id = variant_option_20.id




        variant_media_1 = {
            "variant_option_id": variant_option_1_id,
            "url": "https://images.pexels.com/photos/1545590/pexels-photo-1545590.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }

        variant_media_2 = {
            "variant_option_id": variant_option_2_id,
            "url": "https://images.pexels.com/photos/1375736/pexels-photo-1375736.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }

        variant_media_3 = {
            "variant_option_id": variant_option_3_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_4 = {
            "variant_option_id": variant_option_4_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_5 = {
            "variant_option_id": variant_option_5_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_6 = {
            "variant_option_id": variant_option_6_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_7 = {
            "variant_option_id": variant_option_7_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_8 = {
            "variant_option_id": variant_option_8_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_9 = {
            "variant_option_id": variant_option_9_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_10 = {
            "variant_option_id": variant_option_10_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_11 = {
            "variant_option_id": variant_option_11_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_12 = {
            "variant_option_id": variant_option_12_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_13 = {
            "variant_option_id": variant_option_13_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_14 = {
            "variant_option_id": variant_option_14_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_15 = {
            "variant_option_id": variant_option_15_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_16 = {
            "variant_option_id": variant_option_16_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_17 = {
            "variant_option_id": variant_option_17_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_18 = {
            "variant_option_id": variant_option_18_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_19 = {
            "variant_option_id": variant_option_19_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }
        variant_media_20 = {
            "variant_option_id": variant_option_20_id,
            "url": "https://images.pexels.com/photos/1148957/pexels-photo-1148957.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "format_item": "image/png",
            "position": 0,
        }

        db.session.add(VariantMedias(**variant_media_1))
        db.session.add(VariantMedias(**variant_media_2))
        db.session.add(VariantMedias(**variant_media_3))
        db.session.add(VariantMedias(**variant_media_4))
        db.session.add(VariantMedias(**variant_media_5))
        db.session.add(VariantMedias(**variant_media_6))
        db.session.add(VariantMedias(**variant_media_7))
        db.session.add(VariantMedias(**variant_media_8))
        db.session.add(VariantMedias(**variant_media_9))
        db.session.add(VariantMedias(**variant_media_10))
        db.session.add(VariantMedias(**variant_media_11))
        db.session.add(VariantMedias(**variant_media_12))
        db.session.add(VariantMedias(**variant_media_13))
        db.session.add(VariantMedias(**variant_media_14))
        db.session.add(VariantMedias(**variant_media_15))
        db.session.add(VariantMedias(**variant_media_16))
        db.session.add(VariantMedias(**variant_media_17))
        db.session.add(VariantMedias(**variant_media_18))
        db.session.add(VariantMedias(**variant_media_19))
        db.session.add(VariantMedias(**variant_media_20))
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
