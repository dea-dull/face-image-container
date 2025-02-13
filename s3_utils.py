import boto3
import os
import logging

# Initialize S3 client
s3_client = boto3.client('s3')

def download_image_from_s3(s3_key, bucket_name):
    """
    Download an image from S3.
    """
    download_path = f"/tmp/{s3_key.replace('/', '_')}"  # Unique temp path
    try:
        s3_client.download_file(bucket_name, s3_key, download_path)
        logging.info(f"Image downloaded successfully: {s3_key}")
        return download_path
    except Exception as e:
        logging.error(f"Error downloading image: {e}")
        return None
