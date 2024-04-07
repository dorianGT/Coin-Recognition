import cv2
import numpy as np
import os

folder_path = "Dataset2"
for filename in os.listdir(folder_path):
    if filename.endswith((".jpg", ".jpeg", ".png", ".HEIC")):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)

        # Convertir l'image en espace de couleur HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Seuillage pour la couleur jaune
        lower_yellow = np.array([18, 90, 90])
        upper_yellow = np.array([25, 210, 230])
        mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        # Seuillage pour la couleur rouge
        lower_red = np.array([3, 100, 60])
        upper_red = np.array([10, 210, 230])
        mask_red = cv2.inRange(hsv_image, lower_red, upper_red)

        # Seuillage pour la couleur grise (adapter les plages selon les besoins)
        lower_gray = np.array([3, 10, 100])
        upper_gray = np.array([140, 55, 220])
        mask_gray = cv2.inRange(hsv_image, lower_gray, upper_gray)

        image_segmentee_rouge = cv2.bitwise_and(image, image, mask=mask_red)
        image_segmentee_jaune = cv2.bitwise_and(image, image, mask=mask_yellow)
        image_segmentee_gris = cv2.bitwise_and(image, image, mask=mask_gray)

        # Compter le nombre de pixels dans les régions de couleur rouge, jaune et grise
        red_pixel_count = cv2.countNonZero(mask_red)
        yellow_pixel_count = cv2.countNonZero(mask_yellow)
        gray_pixel_count = cv2.countNonZero(mask_gray) 

        if gray_pixel_count > 0.5 * image[:,:,0].size:
            print("1 euro")
        elif 0.15 * image[:,:,0].size < gray_pixel_count < 0.4 * image[:,:,0].size:
            print("2 euros")
        elif yellow_pixel_count > 0.5 * image[:,:,0].size:
            print(" piece jaune 1e intervalle")
        elif red_pixel_count > 0.5 * image[:,:,0].size:
            print("piece rouge 1e intervalle")
        else:
            lower_yellow = np.array([11, 120, 90])
            upper_yellow = np.array([17, 210, 255])
            mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

            lower_red = np.array([10, 100, 60])
            upper_red = np.array([17, 210, 230])
            mask_red = cv2.inRange(hsv_image, lower_red, upper_red)

            image_segmentee_rouge = cv2.bitwise_and(image, image, mask=mask_red)
            image_segmentee_jaune = cv2.bitwise_and(image, image, mask=mask_yellow)

            red_pixel_count = cv2.countNonZero(mask_red)
            yellow_pixel_count = cv2.countNonZero(mask_yellow)
        
            if red_pixel_count > 0.5 * image[:,:,0].size:
                print(" piece rouge 2e intervalle")
            elif yellow_pixel_count > 0.5 * image[:,:,0].size:
                print("piece jaune 2e intervalle")
            
            else:
                print(" jsp")
        image = cv2.resize(image, (500, 500))
        image_segmentee_rouge = cv2.resize(image_segmentee_rouge,  (500, 500))
        image_segmentee_jaune = cv2.resize(image_segmentee_jaune, (500, 500))
        image_segmentee_gris = cv2.resize(image_segmentee_gris, (500, 500))
        cv2.imshow("Image", image)
        cv2.imshow("rouge", image_segmentee_rouge)
        cv2.imshow("jaune", image_segmentee_jaune)
        cv2.imshow("gris", image_segmentee_gris)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
            
