import cv2
import numpy as np
from insightface import app
from insightface.data import get_dataset

def extract_embeddings(image_path):
    # Load the image
    img = cv2.imread(image_path)

    if img is None:
        raise Exception(f"Error: Image not found at {image_path}")

    # Initialize InsightFace model (assuming the default model)
    detector = app.FaceAnalysis()
    detector.prepare(ctx_id=0)  # Use CPU (ctx_id=0) or GPU (ctx_id=1)

    # Detect faces in the image
    faces = detector.get(img)
    
    if len(faces) == 0:
        raise Exception("No faces detected in the image.")

    # Extract embeddings for the first detected face (you can loop for multiple faces if needed)
    embeddings = faces[0].embedding

    return embeddings

def save_embeddings(embeddings, file_path="/home/ec2-user/face-image/embedding.npy"):
    # Save the embeddings to a .npy file
    np.save(file_path, embeddings)
    print(f"Embeddings saved to {file_path}")

def main(image_path):
    try:
        embeddings = extract_embeddings(image_path)
        save_embeddings(embeddings)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = "download.jpeg"  # Change to the path of the image you want to process
    main(image_path)

