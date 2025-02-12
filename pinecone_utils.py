
import pinecone
import uuid
from config import API_KEY, INDEX_NAME

# Initialize Pinecone
pc = Pinecone(api_key=API_KEY)
index = pc.Index(INDEX_NAME)


def upload_embeddings_to_pinecone(embeddings, metadata, namespace="default"):
    """
    Uploads multiple facial embeddings to Pinecone.
    - Generates unique IDs for each embedding.
    - Formats data to match Pinecone's expected structure.
    - Supports namespaces for logical separation.
    """
    vectors = [
        {
            "id": f"{metadata['face_id']}_{uuid.uuid4().hex[:8]}",  # Unique ID
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


