import matplotlib.pyplot as plt
import cv2

def plot_grayscale_comparison(original_img, gray_img, title="Member 01: Preprocessing View"):
    """
    Displays the Original and Grayscale images side by side using Matplotlib.
    Contributed by: Member 01
    """
    # Convert original BGR to RGB for correct colors in Matplotlib
    original_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))
    
    # Plot Original Image
    axes[0].imshow(original_rgb)
    axes[0].set_title("Original Signing Sheet")
    axes[0].axis("off")
    
    # Plot Grayscale Image
    axes[1].imshow(gray_img, cmap='gray')
    axes[1].set_title("Grayscale Processed")
    axes[1].axis("off")
    
    plt.suptitle(title, fontsize=14)
    plt.tight_layout()
    plt.show()