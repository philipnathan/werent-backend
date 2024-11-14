from flask import Flask, jsonify
from flask_migrate import Migrate
from config import config

from .models import (
    Districts,
    Products,
    RentDetails,
    ReviewLikes,
    ReviewMedias,
    Reviews,
    ShipmentAddresses,
    Stores,
    Transactions,
    UserCarts,
    UserWishlists,
    Users,
    VariantMedias,
    VariantOptions,
)

from .db import db

migrate = Migrate()


def create_app(config_name="default"):

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify("Hello, Dunia!")

    return app
