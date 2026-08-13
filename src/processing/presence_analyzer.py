import cv2

def check_presence(cropped_binary):
    # Count ink pixels. If > 500, student signed.
    ink_pixels = cv2.countNonZero(cropped_binary)
    status = 'Present' if ink_pixels > 500 else 'Absent'
    return status, ink_pixels