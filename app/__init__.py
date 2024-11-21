from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from flask_cors import CORS
from app.config import config

from app.controllers.reviews import reviews_blueprint
from app.controllers.products import products_blueprint

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

from .controllers import users_routes

from .db import db

migrate = Migrate()
jwt = JWTManager()


def create_app(config_name="default"):

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    app.register_blueprint(users_routes)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    Swagger(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(reviews_blueprint)
    app.register_blueprint(products_blueprint)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify("Hello, Dunia!")

    return app
