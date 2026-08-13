import matplotlib.pyplot as plt

def plot_cropped_signature(cropped_img):
    plt.figure(figsize=(5, 5))
    plt.imshow(cropped_img, cmap='gray')
    plt.title('Extracted Signature ROI')
    plt.axis('off')
    plt.savefig('output_member_6.png')
    print('Saved image as output_member_6.png')
    plt.show()