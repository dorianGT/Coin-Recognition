import cv2
import numpy as np
import os

folder_path = "Dataset"  # Replace with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith((".jpg", ".jpeg", ".png", ".HEIC")):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)

        # Convertir l'image en espace de couleur HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Seuillage pour la couleur jaune
        lower_yellow = np.array([20, 120, 120])
        upper_yellow = np.array([30, 255, 255])
        mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        # Seuillage pour la couleur rouge
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask_red = cv2.inRange(hsv_image, lower_red, upper_red)

        # Combinaison des masques jaune et rouge
        masque_final = mask_yellow | mask_red

        # Application du masque à l'image originale
        image_segmentée = cv2.bitwise_and(image, image, mask=masque_final)

        image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)
        image_segmentée = cv2.resize(image_segmentée, (0, 0), fx=0.3, fy=0.3)

        # Affichage de l'image segmentée
        cv2.imshow(image_path, image)
        cv2.imshow(image_path+" segmenté", image_segmentée)
        cv2.waitKey(0)
        cv2.destroyAllWindows()