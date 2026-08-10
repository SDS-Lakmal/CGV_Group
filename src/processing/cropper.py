import cv2

def crop_signature(image, box):
    # Extract the exact ROI of the signature
    x, y, w, h = box
    cropped = image[y:y+h, x:x+w]
    return cropped