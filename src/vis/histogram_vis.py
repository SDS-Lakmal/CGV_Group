import matplotlib.pyplot as plt

def plot_filtering_comparison(gray_img, blurred_img):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].hist(gray_img.ravel(), bins=256, color='black')
    axes[0].set_title('Original Histogram')
    axes[1].hist(blurred_img.ravel(), bins=256, color='blue')
    axes[1].set_title('Filtered Histogram')
    plt.savefig('output_member_2.png')
    print('Saved image as output_member_2.png')
    plt.show()