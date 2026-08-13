import cv2
import matplotlib.pyplot as plt


def plot_bounding_boxes(original, boxes):
    img_copy = original.copy()
    for x, y, w, h in boxes:
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
    plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
    plt.title("Detected Grid Cells")
    plt.savefig("output_member_5.png")
    print("Saved image as output_member_5.png")
    # plt.show()