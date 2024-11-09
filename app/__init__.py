from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
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
