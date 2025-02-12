
import boto3
import os

# Initialize S3 client
s3_client = boto3.client('s3')

def download_image_from_s3(s3_key, BUCKET_NAME):
    """
    Download an image from S3 using the given S3 key and bucket name.
    """
    download_path = '/tmp/temp_image.jpg'  # Temporary storage
    try:
        s3_client.download_file(BUCKET_NAME, s3_key, download_path)
        print(f"Image downloaded successfully: {s3_key}")
        return download_path
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

