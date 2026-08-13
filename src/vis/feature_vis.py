import cv2
import matplotlib.pyplot as plt

def plot_keypoints(image, keypoints):
    img_with_kp = cv2.drawKeypoints(image, keypoints, None, color=(0,255,0))
    plt.figure(figsize=(8, 10))
    plt.imshow(cv2.cvtColor(img_with_kp, cv2.COLOR_BGR2RGB))
    plt.title('Signature Feature Keypoints')
    plt.savefig('output_member_9.png')
    print('Saved image as output_member_9.png')
    plt.show()