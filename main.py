

import os
from s3_utils import download_image_from_s3
from facial_recognition import extract_embeddings
from pinecone_utils import upload_embeddings_to_pinecone
from config import BUCKET_NAME, ORGANIZATION_NAME
from utils import cleanup_file
import numpy as np



def main():
    # Get the S3 key from environment variables
    s3_key = os.getenv("S3_KEY")

    if not s3_key:
        print("Error: No S3 key provided.")
        return

    # Step 1: Download the image from S3
    image_path = download_image_from_s3(s3_key, BUCKET_NAME)
    if not image_path:
        print("Failed to download image. Exiting.")
        return

    # Step 2: Extract facial embeddings
    try:
        embeddings = extract_embeddings(image_path)

        if not embeddings:
            print("No face detected. Exiting.")
            return
    except Exception as e:
        print(f"Error processing image: {e}")
        return

    # Step 3: Upload embeddings to Pinecone
    metadata = {"image_id": s3_key, "organization": ORGANIZATION_NAME}
    upload_embeddings_to_pinecone(embeddings, metadata, image_path, namespace="default")

    # Step 4: Cleanup
    cleanup_file(image_path)

if __name__ == "__main__":
    main()
