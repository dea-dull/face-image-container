
import cv2
import numpy as np
import logging
from insightface.app import FaceAnalysis

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize InsightFace model **once** at the top
face_model = FaceAnalysis()
face_model.prepare(ctx_id=-1, det_size=(640, 640))  # Use default detection size

def preprocess_image(image_path):
    """
    Preprocess the image:
    - Convert BGR to RGB (InsightFace expects RGB input)
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Unable to read the image at path: {image_path}")

    # Convert BGR to RGB (InsightFace expects RGB input)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image

def extract_embeddings(image_path):
    """
    Extract facial embeddings from an image.
    """
    image = preprocess_image(image_path)

    # Run face detection and get embeddings
    results = face_model.get(image)

    if not results:
        logging.warning("No face detected in the image.")
        return []

    return [
        {
            "embedding": face.normed_embedding.tolist(),  # Use normalized embedding
            "bbox": face.bbox.tolist()
        }
        for face in results
    ]
