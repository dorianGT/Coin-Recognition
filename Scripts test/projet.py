
import numpy as np
import cv2
import os

folder_path = "Dataset"  # Replace with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".HEIC"):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        #Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #Appliquer un flou median
        blurred_image = cv2.medianBlur(gray, 3)

        #Appliquer la binarisation adaptative
        binary_image = cv2.adaptiveThreshold(blurred_image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,801,2)

        #Elements structurants
        kernel_e = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,3))
        kernel_d = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,2))
        kernel_f = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,4))

        #Erode et dilatation
        #eroded_image = cv2.erode(binary_image, kernel_e, iterations=1)
        #dilated_image = cv2.dilate(binary_image, kernel_d, iterations=1)
        #image_close = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel_f)

        contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Créer une liste pour stocker les contours filtrés par taille
        filtered_contours = []

        #La taille minimale des cc à conserver
        min_contour_size = 3000

        #Filtrer les contours par taille
        for contour in contours:
            if cv2.contourArea(contour) > min_contour_size:
                filtered_contours.append(contour)

        #Créer une image vide pour dessiner les contours filtrés
        #filtered_contour_image = image.copy()
        filtered_contour_image = np.ones_like(image) * 255 #une copie blanche

        #Supprimer le + grand contours (la fenetre)
        largest_contour_index = max(range(len(filtered_contours)), key=lambda i: cv2.contourArea(filtered_contours[i]))
        del filtered_contours[largest_contour_index]

        #Dessiner les contours  sur l'image vide
        cv2.drawContours(filtered_contour_image, filtered_contours, -1, (0, 255, 0), -1) #en vert
        #cv2.drawContours(filtered_contour_image, filtered_contours, -1, (0, 0, 0), thickness=2) # en noir

        #Remplir l'intérieur des pièces
        #for contour in filtered_contours:
        #    cv2.fillPoly(filtered_contour_image, pts=[contour], color=(0, 0, 0))


        #Créer une image vide pour dessiner les contours externes
        external_contour_image = image.copy() #une copie blanche

        #Trouver les contours externes des objets
        external_contours = []
        for contour in filtered_contours:
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            external_contours.append(approx)

        #Dessiner les contours externes sur l'image vide
        cv2.drawContours(external_contour_image, external_contours, -1, (0, 255, 0), thickness=2) # en vert


        #Redimensionner l'image pour l'affichage
        binary_image = cv2.resize(binary_image, (0,0), fx=0.3, fy=0.3)
        #image_close = cv2.resize(image_close, (0,0), fx=0.3, fy=0.3)
        filtered_contour_image = cv2.resize(filtered_contour_image, (0,0), fx=0.3, fy=0.3)
        external_contour_image = cv2.resize(external_contour_image, (0,0), fx=0.3, fy=0.3)

        #Afficher l'image avec les contours filtrés par taille
        cv2.imshow('image binaire', binary_image) 
        #cv2.imshow('image binaire filtre', image_close) 
        cv2.imshow('Contours filtrés par taille', filtered_contour_image) 
        cv2.imshow("External Contour Image", external_contour_image)
        cv2.waitKey(0) 

