import matplotlib.pyplot as plt

def plot_morphology(cleaned_img):
    plt.figure(figsize=(6, 8))
    plt.imshow(cleaned_img, cmap='gray')
    plt.title('Morphological Cleaning Result')
    plt.axis('off')
    plt.savefig('output_member_4.png')
    print('Saved image as output_member_4.png')
    # plt.show()