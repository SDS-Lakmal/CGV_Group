import cv2
import numpy as np

def clean_noise(binary_image):
    # Remove small white dots (noise) using morphological closing
    kernel = np.ones((3,3), np.uint8)
    cleaned = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    return cleaned