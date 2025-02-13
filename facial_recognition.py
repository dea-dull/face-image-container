import cv2
import numpy as np
import logging
from insightface.app import FaceAnalysis

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize InsightFace model **once** at the top (avoid reloading on each call)
face_model = FaceAnalysis(providers=['CPUExecutionProvider'])

def preprocess_image(image_path):
    """
    Preprocess the image:
    - Convert BGR to RGB
    - Resize if too large
    - Normalize pixel values
    - Determine detection size dynamically
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Unable to read the image at path: {image_path}")

    # Convert BGR to RGB (InsightFace expects RGB input)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Get original size
    height, width = image.shape[:2]

    # Dynamically set detection size (limit max size to avoid memory issues)
    max_size = 1024  # Max size for width/height
    if max(height, width) > max_size:
        scale_factor = max_size / max(height, width)
        new_size = (int(width * scale_factor), int(height * scale_factor))
        image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
        logging.info(f"Resized image to {new_size}")
    else:
        new_size = (width, height)

    # Normalize pixel values (optional, useful for some models)
    image = image.astype(np.float32) / 255.0  # Scale to [0,1]

    return image, new_size

def extract_embeddings(image_path):
    """
    Extract facial embeddings from a preprocessed image.
    """
    image, det_size = preprocess_image(image_path)

    # Prepare the model with dynamic detection size
    face_model.prepare(ctx_id=0, det_size=det_size)

    results = face_model.get(image)
    
    if not results:
        logging.warning("No face detected in the image.")
        return []

    return [
        {
            "embedding": face.embedding.tolist(),
            "bbox": face.bbox.tolist()
        }
        for face in results
    ]
