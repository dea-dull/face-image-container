import cv2
import numpy as np
import logging
from deepface import DeepFace

# Initialize logging
logging.basicConfig(level=logging.INFO)

def preprocess_image(image_path):
    """
    Preprocess the image:
    - Convert BGR to RGB (DeepFace expects RGB input)
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Unable to read the image at path: {image_path}")

    # Convert BGR to RGB (DeepFace expects RGB input)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image


def extract_embeddings(image_path):
    """
    Extract facial embeddings and bounding boxes from an image using OpenCV and DeepFace.
    """
    image = preprocess_image(image_path)

    # Use OpenCV to detect faces and get bounding boxes
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Run DeepFace to extract embeddings
    try:
        embeddings = DeepFace.represent(img_path=image_path, model_name="Facenet", enforce_detection=True)
        if not embeddings:
            logging.warning("No face detected in the image.")
            return []

        # Add bounding boxes and embeddings
        return [
            {
                "embedding": face["embedding"],  # Extracted embeddings
                "bbox": [x, y, w, h]  # OpenCV bounding box coordinates
            }
            for (x, y, w, h), face in zip(faces, embeddings)
        ]

    except Exception as e:
        logging.error(f"Error in embedding extraction: {str(e)}")
        return []
