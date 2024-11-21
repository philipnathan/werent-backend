from app.db import db
from app.models import VariantOptions, VariantMedias


class VariantOptionsRepository:
    def __init__(
        self, variant_option=VariantOptions, variant_media=VariantMedias, db=db
    ):
        self.variant_option = variant_option
        self.variant_media = variant_media
        self.db = db

    def create_variant_option(self, data):
        return self.variant_option(**data)

    def create_variant_media(self, media_data):
        return self.variant_media(**media_data)
