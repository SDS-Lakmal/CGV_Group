from skimage.metrics import structural_similarity as ssim
import cv2

def compare_signatures(img1, img2):
    # Compare if two signatures belong to the same person
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    score, diff = ssim(img1, img2_resized, full=True)
    return score