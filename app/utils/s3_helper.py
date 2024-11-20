import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError
import time
from werkzeug.utils import secure_filename

load_dotenv(override=True)


class S3Helper:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION_NAME"),
        )
        self.bucket_name = os.getenv("AWS_BUCKET_NAME")

    def generate_s3_key(self, filename, prefix):
        """
        Genrate unique S3 key
        """
        timestamp = int(time.time())
        safe_filename = secure_filename(filename)
        return f"{prefix}/{timestamp}-{safe_filename}"

    def upload_file(self, file_obj, object_key):
        """
        Uploads a file to an S3 bucket
        file_object: File to be uploaded
        object_name: Name of the object in the S3 bucket
        """
        try:
            self.s3_client.upload_fileobj(
                Fileobj=file_obj,
                Bucket=os.getenv("AWS_BUCKET_NAME"),
                Key=object_key,
                ExtraArgs={"ContentType": file_obj.content_type},
            )
            return {"success": True}
        except ClientError as e:
            return {"error": str(e), "success": False}

    def read_file(self, object_key):
        """
        Reads a file from an S3 bucket based on the object name
        """

        try:
            response = self.s3_client.list_objects_v2(
                Bucket=os.getenv("AWS_BUCKET_NAME"), Prefix="reviews"
            )
            return {"success": True, "data": response}
        except ClientError as e:
            return {"error": str(e), "success": False}
