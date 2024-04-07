import cv2
import numpy as np
import os

def detect_coins(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to remove noise
    blurred = cv2.GaussianBlur(gray, (15,15), 0)
    
    # Apply HoughCircles to detect circles in the image
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=120, param2=50, minRadius=50, maxRadius=100)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        
        for i in circles[0, :]:
            cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)
    img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
    cv2.imshow('Detected Coins', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

folder_path = "Dataset"  # Remplacez par le chemin de votre dossier

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".HEIC"):
        image_path = os.path.join(folder_path, filename)
        detect_coins(image_path)

