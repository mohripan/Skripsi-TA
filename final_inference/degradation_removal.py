import cv2
import os

# Set the path for your images
folder_path = 'degradationremoval'

# List all files in the directory
for filename in os.listdir(folder_path):
    # Ensure we're working with an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Read the image
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)

        # Blur the image (using Gaussian blur)
        blurred_image = cv2.GaussianBlur(image, (25, 25), 0)

        # Overwrite the original image
        cv2.imwrite(image_path, blurred_image)