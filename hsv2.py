import numpy as np
import cv2
import os

folder_path = "Dataset"  # Replace with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith((".jpg", ".jpeg", ".png", ".HEIC")):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        # Neutralize luminance
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # Darken the image
        hsv[:,:,2] = hsv[:,:,2] * 0.3  # Multiply the V channel by 0.8 to darken the image

        # Enhance the edges
        blurred = cv2.GaussianBlur(hsv[:,:,2], (55, 55), 0)
        edges = cv2.Canny(blurred, 100, 200)

        # Combine the original V channel with the enhanced edges
        hsv[:,:,2] = np.maximum(hsv[:,:,2], edges)

        # Convert back to BGR
        image_darkened = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        # Binarize the enhanced image using Otsu's thresholding
        gray_image = cv2.cvtColor(image_darkened, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)
        image_darkened = cv2.resize(image_darkened, (0, 0), fx=0.3, fy=0.3)
        cv2.imshow('Original Image', image)
        cv2.imshow('Darkened Image with Enhanced Edges', image_darkened)
        binary_image = cv2.resize(binary_image, (0, 0), fx=0.3, fy=0.3)
        cv2.imshow('Binarized Image', binary_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()