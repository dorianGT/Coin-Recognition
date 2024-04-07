import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

folder_path = "Dataset"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".HEIC"):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.medianBlur(gray, 31)
        binary_image = cv2.adaptiveThreshold(blurred_image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,801,2)

        kernel = np.ones((3,3), np.uint8)
        opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel=kernel, iterations=2)

        contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Créer une liste pour stocker les contours filtrés par taille
        filtered_contours = []

        #La taille minimale des cc à conserver
        min_contour_size = 3000

        #Filtrer les contours par taille
        for contour in contours:
            if cv2.contourArea(contour) > min_contour_size:
                filtered_contours.append(contour)

        #Supprimer le + grand contours (la fenetre)
        largest_contour_index = max(range(len(filtered_contours)), key=lambda i: cv2.contourArea(filtered_contours[i]))
        del filtered_contours[largest_contour_index]

        filtered_contour_image = np.ones_like(image) * 0 
        for contour in filtered_contours:
            cv2.fillPoly(filtered_contour_image, pts=[contour], color=(255, 255, 255))
            
        opening = filtered_contour_image
        opening = cv2.cvtColor(opening, cv2.COLOR_BGR2GRAY)

        dist_transform = cv2.distanceTransform(src=opening, distanceType=cv2.DIST_L2, maskSize=5)
        # plt.figure()
        # plt.title("Distance Transform")
        # plt.imshow(dist_transform, cmap="gray")
        # plt.axis("off")
        # plt.show()

        #----------------------------------------------------------------------------------------------------------------#

        ret, sure_foreground = cv2.threshold(src=dist_transform, thresh=0.4*np.max(dist_transform), maxval=255, type=0)
        sure_background = cv2.dilate(src=opening, kernel=kernel, iterations=1) #int
        sure_foreground = np.uint8(sure_foreground) # change its format to int
        unknown = cv2.subtract(sure_background, sure_foreground)
        ret, marker = cv2.connectedComponents(sure_foreground)
        marker = marker + 1
        marker[unknown == 255] = 0 # White area is turned into Black to find island for watershed
        marker = cv2.watershed(image, markers=marker)
        contour, hierarchy = cv2.findContours(image=marker.copy(), mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(contour)):
            
            if hierarchy[0][i][3] == -1:
                cv2.drawContours(image,contours=contour,contourIdx=i, color=(255,0,0), thickness=5)

        image = cv2.resize(image, (0,0), fx=0.3, fy=0.3)
        cv2.imshow('cc', image) 
        cv2.waitKey(0) 
