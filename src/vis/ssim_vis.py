import matplotlib.pyplot as plt

def plot_similarity_score(score):
    plt.figure(figsize=(5, 5))
    plt.bar(['SSIM Score'], [score], color='purple')
    plt.ylim(0, 1.0)
    plt.title(f'Signature Match Score: {score:.2f}')
    plt.savefig('output_member_10.png')
    print('Saved image as output_member_10.png')
    # plt.show()