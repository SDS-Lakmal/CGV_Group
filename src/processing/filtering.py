import cv2

def apply_noise_filtering(gray_image):
    # Apply Gaussian Blur to remove scanner noise
    blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
    median = cv2.medianBlur(blurred, 3)
    return blurred, median