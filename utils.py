import os

def cleanup_file(file_path):
    """
    Deletes a temporary file after processing.
    """
    try:
        os.remove(file_path)
        print(f"Deleted temporary file: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {e}")

