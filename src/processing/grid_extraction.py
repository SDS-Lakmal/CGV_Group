import cv2


def find_signature_boxes(cleaned_image):
    # Find table contours
    contours, _ = cv2.findContours(
        cleaned_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    boxes = [
        cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 1000
    ]
    return boxes