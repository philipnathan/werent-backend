import os
from app.db import db
from app.utils import S3Helper
from app.models import Products
from .variant_options_repository import VariantOptionsRepository
from app.config import Config


class VariantOptionsService:
    def __init__(
        self,
        db=db,
        s3_helper=S3Helper,
        product=Products,
        repository=VariantOptionsRepository(),
        config=Config,
    ):
        self.db = db
        self.s3_helper = s3_helper
        self.product = product
        self.repository = repository
        self.config = config

    def create_variant_option(self, form, product_id):
        try:
            properties = [
                "variant_name",
                "total_stock",
                "price",
                "bust",
                "length",
            ]

            data = {}
            for prop in properties:
                if form.get(prop) is None:
                    raise ValueError(f"{prop} is required")

                data[prop] = form.get(prop)

            if self.product.query.get(product_id) is None:
                raise ValueError("Product not found")

            data["product_id"] = product_id

            variant_option = self.repository.create_variant_option(data=data)

            self.db.session.add(variant_option)
            self.db.session.flush()

            medias = form.get("media")
            if medias and len(medias) > self.config.MAX_NUMBER_OF_REVIEW_MEDIA:
                raise ValueError(
                    "Maximum number of media files exceeded (maximum is 3)"
                )

            if medias:
                self._upload_variant_media(medias, variant_option.id)

            self.db.session.commit()
            return {
                "message": "Variant option created successfully",
                "variant_option": variant_option.to_dict(),
            }, 201

        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def _upload_variant_media(self, medias, variant_option_id):
        for file in medias:
            if file and file.filename:
                # Validate each file
                self._validate_media(file)

        all_media = []
        for file in medias:
            position = 0
            if file and file.filename:

                # Generate S3 key
                s3_key = self.s3_helper.generate_s3_key(
                    filename=file.filename, prefix="variant_options"
                )

                # upload file to S3
                result = self.s3_helper.upload_file(file_obj=file, object_key=s3_key)

                if result["success"]:
                    all_media.append(
                        {
                            "variant_option_id": variant_option_id,
                            "url": f"https://{os.getenv('AWS_BUCKET_NAME')}.s3.ap-southeast-3.amazonaws.com/{s3_key}",
                            "format_media": file.content_type,
                            "position": position,
                        }
                    )
                    position += 1
                else:
                    raise Exception(f"Failed to upload file: {result.get('error')}")

            if all_media:
                media_objects = [
                    self.repository.create_variant_media(media_data=media)
                    for media in all_media
                ]

                self.db.session.add_all(media_objects)

    def _validate_media(self, media):
        """
        validate a single media against configured constraints
        """

        # Check file extension
        ext = os.path.splitext(media.filename)[1][1:].lower()
        if ext not in Config.ALLOWED_EXTENSIONS_REVIEW_MEDIA:
            raise ValueError(
                f"File type '.{ext}' not allowed. Allowed types: {', '.join(Config.ALLOWED_EXTENSIONS_REVIEW_MEDIA)}"
            )

        # Check file size
        media.seek(0, os.SEEK_END)
        size = media.tell()
        media.seek(0)  # Reset file pointer

        if size > Config.MAX_FILE_SIZE_REVIEW_MEDIA:
            max_size_mb = Config.MAX_FILE_SIZE_REVIEW_MEDIA / (1024 * 1024)
            raise ValueError(
                f"File size exceeds maximum allowed size of {max_size_mb}MB"
            )

        return True
