import uuid
import os

from dotenv import load_dotenv

from .reviews_repository import ReviewRepository
from app.utils import S3Helper
from app.config import Config
from app.db import db

load_dotenv(override=True)


class ReviewService:
    def __init__(self, review_repository=ReviewRepository, s3_helper=S3Helper, db=db):

        self.review_repository = review_repository()
        self.s3_helper = s3_helper()
        self.db = db

    def get_product_reviews(self, product_id):
        reviews = self.review_repository.get_reviews(product_id=product_id)
        return [review.to_dict() for review in reviews]

    def add_review(self, user_id, form, medias, product_id):
        try:
            if "rating" not in form:
                raise ValueError("Rating is required")
            if "comment" not in form:
                raise ValueError("Comment is required")

            # Create review id
            review_id = str(uuid.uuid4())

            # Create review
            review_data = {
                "id": f"{review_id}",
                "user_id": user_id,
                "product_id": product_id,
                "rating": form.get("rating"),
                "comment": form.get("comment"),
            }

            review = self.review_repository.create_review(review_data=review_data)

            # Handle media upload if any
            if medias and len(medias) > Config.MAX_NUMBER_OF_REVIEW_MEDIA:
                raise ValueError(
                    "Maximum number of media files exceeded (maximum is 3)"
                )

            if medias:
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
                            filename=file.filename, prefix="reviews"
                        )

                        # upload file to S3
                        result = self.s3_helper.upload_file(
                            file_obj=file, object_key=s3_key
                        )

                        if result["success"]:
                            all_media.append(
                                {
                                    "review_id": f"{review_id}",
                                    "url": f"https://{os.getenv('AWS_BUCKET_NAME')}.s3.ap-southeast-3.amazonaws.com/{s3_key}",
                                    "format_media": file.content_type,
                                    "position": position,
                                }
                            )
                        else:
                            raise Exception(
                                f"Failed to upload file: {result.get('error')}"
                            )

                if all_media:
                    media_objects = [
                        self.review_repository.create_review_media(media_data=media)
                        for media in all_media
                    ]
                    self.db.session.add_all(media_objects)

            self.db.session.add(review)
            self.db.session.commit()

            return {"message": "Review created successfully"}, 201

        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

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

    def get_reviews(self):
        all_reviews = self.review_repository.get_reviews()

        return [review.to_dict() for review in all_reviews]
