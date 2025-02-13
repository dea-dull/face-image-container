
import boto3
import json
import os
from dotenv import load_dotenv

# AWS region where the secret is stored
# AWS_REGION = "us-west-2"  # Change to your AWS region
# SECRET_NAME = "MyPineconeSecret"

# def get_secrets():
#     """
#     Fetch API_KEY and INDEX_NAME securely from AWS Secrets Manager.
#     """
#     try:
#         # Create a Secrets Manager client
#         client = boto3.client("secretsmanager", region_name=AWS_REGION)

#         # Retrieve the secret
#         response = client.get_secret_value(SecretId=SECRET_NAME)

#         # Parse the secret JSON
#         secret_data = json.loads(response["SecretString"])
        
#         return secret_data

#     except Exception as e:
#         print(f"Error retrieving secret: {e}")
#         return None

# # Fetch secrets (only call this in production)
# secrets = get_secrets()
# if secrets:
#     API_KEY = secrets["API_KEY"]
#     INDEX_NAME = secrets["INDEX_NAME"]
#     BUCKET_NAME = secrets["BUCKET_NAME"]
# else:
#     API_KEY = os.getenv("API_KEY")  # Fallback for local dev
#     INDEX_NAME = os.getenv("INDEX_NAME")



# Load environment variables from .env file
load_dotenv()

# S3 Configuration
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Pinecone Configuration
API_KEY = os.getenv("API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")

# General Metadata
ORGANIZATION_NAME = os.getenv("ORGANIZATION_NAME")


