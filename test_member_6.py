import cv2
from src.processing.cropper import crop_signature
from src.vis.crop_vis import plot_cropped_signature

# 1. Load Real Image
real_img = cv2.imread('dataset/1.jpeg')

# Resize image to fit the screen (For testing purposes only)
real_img_resized = cv2.resize(real_img, (800, 1000))

print("Please draw a box around a single signature using your mouse...")
print("Press ENTER or SPACE after drawing the box!")

# 2. Interactive ROI Selection
dummy_box = cv2.selectROI("Select Signature for Report", real_img_resized, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Signature for Report")

# 3. Test Member 6's Actual Logic
if dummy_box[2] > 0 and dummy_box[3] > 0:
    cropped = crop_signature(real_img_resized, dummy_box)
    plot_cropped_signature(cropped)
else:
    print("You did not select a bounding box!") #abcd