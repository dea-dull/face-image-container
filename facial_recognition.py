
import cv2
from insightface.app import FaceAnalysis

# Initialize InsightFace model
app = FaceAnalysis(providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

def extract_embeddings(image_path):
    """
    Extract facial embeddings from an image.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Unable to read the image.")

    results = app.get(image)
    
    if not results:
        raise ValueError("No face detected in the image.")

    # Handle multiple faces: return a list of embeddings
    embeddings = [face.embedding for face in results]
    return embeddings

