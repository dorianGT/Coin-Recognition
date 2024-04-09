# Coin-Recognition

## Présentation du Projet : Détection et Identification de Pièces de Monnaie en Euros

Ce projet vise à développer un système de détection, d'identification et de comptage des pièces de monnaie en euros à partir d'une image donnée en entrée. La tâche est réalisée en plusieurs étapes, notamment l'acquisition de données, l'implémentation d'algorithmes de détection et de classification, ainsi que l'évaluation des performances du système.

## Méthode et Traitement

Acquisition des Données : Nous avons construit un jeu de données comprenant des images représentant des ensembles de pièces de monnaie en euros.

Labélisation des Données : Nous avons labélisé chaque image à l'aide de LabelMe. Chaque image de notre jeu de données est associée à un fichier JSON contenant des informations détaillées sur chaque pièce de monnaie présente dans l'image. Les données labélisées comprennent les coordonnées du centre de la pièce ainsi qu'un point sur le cercle délimitant la pièce. De plus, chaque pièce est étiquetée avec sa valeur monétaire, facilitant ainsi la tâche de classification ultérieure.

Détection des Pièces : Nous avons implémenté une méthode de détection des pièces de monnaie dans une image en utilisant des techniques de vision par ordinateur telles que la détection de contour.

Comptage des Pièces : Une fois les pièces détectées et identifiées, nous avons mis en place un mécanisme de comptage pour calculer la somme totale représentée par les pièces dans l'image.

### Traitement Partie 1: Détection des pièces

![Traitement 1](https://github.com/dorianGT/Coin-Recognition/blob/main/Traitement1.JPG)

### Traitement Partie 2: Trouver la valeur

![Traitement 2](https://github.com/dorianGT/Coin-Recognition/blob/main/Traitement2.JPG)

## Résultats

Après avoir testé notre système sur un ensemble de données d'évaluation, nous avons obtenu des résultats prometteurs en termes de détection. Malgré la précision de la détection, nous avons constaté que le processus de comptage des pièces n'était pas aussi précis que prévu.

![Resultats 1](https://github.com/dorianGT/Coin-Recognition/blob/main/Resultats1.JPG)
![Resultats 3](https://github.com/dorianGT/Coin-Recognition/blob/main/Resultats3.JPG)

### Exemple de tableau obtenu
![Resultats 2](https://github.com/dorianGT/Coin-Recognition/blob/main/Resultats2.JPG)

### Exemple de résultat
![Resultats 2](https://github.com/dorianGT/Coin-Recognition/blob/main/Results/012_jpeg/final.jpg)

## Critique de la Solution Existante et Axes d'Amélioration

Bien que notre système produise des résultats satisfaisants, certaines améliorations peuvent être envisagées pour renforcer ses performances. Parmi ces axes d'amélioration, on peut citer :

- Optimisation de la Précision : Affiner les algorithmes de détection et de classification pour améliorer la précision de l'identification des pièces.

- Gestion des Cas Limites : Renforcer la capacité du système à gérer les cas où les pièces sont partiellement cachées ou enchevêtrées les unes avec les autres.

- Extension à d'Autres Devises : Adapter le système pour qu'il puisse également détecter et identifier des pièces d'autres devises que l'euro, ce qui le rendrait plus polyvalent.
  
- Utilisation du Deep Learning : Utilisation de modèle CNN pour obtenir de meilleur résultat et surtout des résultats plus constant.

En résumé, ce projet représente une première étape vers le développement d'un système robuste et précis de détection et de comptage de pièces de monnaie en euros à partir d'images.

## Utilisation

Le fichier main.ipynb est le fichier regroupant notre solution. Dans le dossier "Results", se trouvent tous les résultats que nous avons obtenus. Pour chaque image, vous pouvez retrouver les images suivantes :

- Originale
- Passage en niveau de gris
- Flou médian
- Flou gaussien
- Finale
- Des pièces trouvées
- Des pièces trouvées étiquetées

