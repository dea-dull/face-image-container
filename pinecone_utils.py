import pinecone
import uuid
import hashlib
from config import API_KEY, INDEX_NAME

# Initialize Pinecone
pc = pinecone.Client(api_key=API_KEY)
index = pc.Index(INDEX_NAME)

def generate_face_id(image_path):
    """Generate a deterministic Face ID using SHA256 hash of the image."""
    try:
        # Open the image and read its bytes
        with open(image_path, "rb") as img_file:
            image_hash = hashlib.sha256(img_file.read()).hexdigest()[:16]  # First 16 chars

        # Generate a unique face ID based on the hash of the image
        return f"face_{image_hash}"
    except Exception as e:
        print(f"Error generating Face ID: {e}")
        return None


def upload_embeddings_to_pinecone(embeddings, metadata, image_path, namespace="default"):
    """
    Uploads facial embeddings to Pinecone with a unique Face ID.
    - Generates a unique ID for each face based on the image.
    """
    # Generate a unique Face ID based on the image
    face_id = generate_face_id(image_path)
    if not face_id:
        print("Error: Failed to generate Face ID. Skipping upload.")
        return
    
    vectors = [
        {
            "id": face_id,  # Use the generated face ID
            "values": embedding.tolist(),
            "metadata": metadata
        }
        for embedding in embeddings
    ]
    
    try:
        index.upsert(vectors=vectors, namespace=namespace)
        print(f"Uploaded {len(vectors)} face embeddings to Pinecone (Namespace: {namespace})")
    except Exception as e:
        print(f"Error uploading to Pinecone: {e}")
