import cv2
import numpy as np

def afficher_image_hsv(image):
  """
  Fonction qui affiche l'image et la valeur HSV du pixel cliqué dans la console.

  Args:
    image: L'image à afficher.

  Returns:
    None.
  """

  # Conversion de l'image en HSV (déplacé à l'intérieur de la fonction)
  hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  # Affichage de l'image
  cv2.imshow("Image", image)

  # Définition du callback pour la gestion du clic
  def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
      # Récupération des coordonnées du pixel cliqué
      pixel_coord = (x, y)

      # Récupération de la valeur HSV du pixel cliqué (utilise hsv_image)
      pixel_hsv = hsv_image[y, x]

      # Affichage de la valeur HSV dans la console
      print(f"Valeur HSV du pixel ({x}, {y}): {pixel_hsv}")

  # Ajout du callback à la fenêtre d'affichage
  cv2.setMouseCallback("Image", on_mouse_click)

import os

folder_path = "Dataset"  # Replace with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith((".jpg", ".jpeg", ".png", ".HEIC")):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)
        image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)
        afficher_image_hsv(image)
          # Attente d'une touche pour quitter
        cv2.waitKey(0)
        cv2.destroyAllWindows()

