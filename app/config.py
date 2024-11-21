import os
from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALLOWED_EXTENSIONS_REVIEW_MEDIA = {"png", "jpg", "jpeg", "mp4", "mov"}
    MAX_FILE_SIZE_REVIEW_MEDIA = 6 * 1024 * 1024  # 6MB
    MAX_NUMBER_OF_REVIEW_MEDIA = 3


class DevelopmentConfig(Config):
    DEBUG = True

    username = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST")
    port = os.getenv("MYSQL_PORT")
    database = os.getenv("MYSQL_DATABASE")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
