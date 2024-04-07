import cv2
import numpy as np
import os


def enhance_edges(image):
    # Appliquer un filtre de renforcement des contours
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    enhanced_image = cv2.filter2D(image, -1, kernel)

    return enhanced_image

def adaptive_otsu_thresholding(image, block_size=505):
    height, width= image.shape
    thresholded_image = np.zeros((height, width), dtype=np.uint8)

    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = image[i:i+block_size, j:j+block_size]
            block_mean = np.mean(block)
            block_variance = np.var(block)

            threshold, _ = cv2.threshold(block, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            adaptive_threshold = block_mean + ((block_variance * threshold) / 256)

            thresholded_image[i:i+block_size, j:j+block_size] = np.where(block >= adaptive_threshold, 255, 0)

    return thresholded_image

# Charger l'image
# image = cv2.imread('Dataset/7.jpg',0)
# image = enhance_edges(image)
# image = cv2.Canny(image, 100, 170)
# Améliorer les contours de l'image
# Appliquer OTSU adaptative
# adaptive_otsu_image = adaptive_otsu_thresholding(image)

# Afficher l'image résultante
# adaptive_otsu_image = cv2.resize(adaptive_otsu_image, (0,0), fx=0.3, fy=0.3)
# cv2.imshow('Adaptive OTSU', adaptive_otsu_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

folder_path = "Dataset"  # Remplacez par le chemin de votre dossier

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".HEIC"):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        # Sharpening the image
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpened_image = cv2.filter2D(image, -1, kernel)
        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        edges = cv2.Canny(gray_image, 100, 200)
        dilated = cv2.dilate(edges, (1,1), iterations = 10)

        # Redimensionner l'image pour l'affichage
        image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)
        sharpened_image = cv2.resize(sharpened_image, (0, 0), fx=0.3, fy=0.3)
        edges = cv2.resize(edges, (0, 0), fx=0.3, fy=0.3)
        dilated = cv2.resize(dilated, (0, 0), fx=0.3, fy=0.3)

        cv2.imshow("Image originale", image)
        cv2.imshow("Image avec accentuation", sharpened_image)
        cv2.imshow("Contours", edges)
        cv2.imshow("dilated", dilated)
        cv2.waitKey(0)

cv2.destroyAllWindows()