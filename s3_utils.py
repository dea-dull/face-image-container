import boto3
import os
import logging
import tempfile
import botocore.exceptions

# Initialize S3 client
s3_client = boto3.client('s3')

# Load environment variables
s3_key = os.getenv("S3_KEY")
bucket_name = os.getenv("BUCKET_NAME")

def download_image_from_s3(s3_key, bucket_name):
    """
    Download an image from S3.
    """
    if not s3_key:
        logging.error("S3_KEY environment variable is missing.")
        return None
    if not bucket_name:
        logging.error("BUCKET_NAME environment variable is missing.")
        return None

    download_path = os.path.join(tempfile.gettempdir(), s3_key.replace('/', '_'))  # Use OS-independent temp directory
    
    try:
        s3_client.download_file(bucket_name, s3_key, download_path)
        logging.info(f"Image downloaded successfully: {s3_key}")
        return download_path
    except botocore.exceptions.NoCredentialsError:
        logging.error("AWS credentials not found. Ensure they are set up correctly.")
    except botocore.exceptions.PartialCredentialsError:
        logging.error("AWS credentials are incomplete.")
    except Exception as e:
        logging.error(f"Unexpected error downloading image: {e}")
    
    return None
