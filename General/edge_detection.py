import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to apply Sobel filter for edge detection
def apply_sobel_filter(image_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: Unable to read image from {image_path}")
        return

    # Apply Sobel filter
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel filter for x-direction
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel filter for y-direction

    # Calculate the gradient magnitude
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel_magnitude = np.uint8(np.clip(sobel_magnitude, 0, 255))

    # Display the original and edge-detected images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(sobel_magnitude, cmap='gray')
    plt.title('Edge Detected Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# Path to your image
image_path = 'path/to/your/image.jpg'

# Apply Sobel filter and display results
apply_sobel_filter(image_path)
