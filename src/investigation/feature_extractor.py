import cv2

def extract_features(image):
    # Extract keypoints using ORB for advanced recognition
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return keypoints, descriptors