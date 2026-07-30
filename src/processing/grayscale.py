import cv2
import os

def load_and_convert_grayscale(image_path):
    """
    Loads an image from the dataset and converts it to Grayscale.
    Contributed by: Member 01
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at: {image_path}")
        
    # Read the original image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Failed to load image. Check file format.")
        
    # Convert BGR image to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray_image