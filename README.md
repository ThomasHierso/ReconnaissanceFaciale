Projet : Reconnaissance faciale en Python

Description :
---------------
Ce projet utilise Python pour détecter et reconnaître des visages à partir d'une webcam. 
Les fonctionnalités incluent la capture de photos, l'encodage des visages connus, 
et l'affichage en temps réel avec rectangles et noms.

Environnement :
---------------
- Python 3.11
- Virtual environment : env311
- Principales bibliothèques utilisées :
  - numpy==1.25.2
  - opencv-python
  - face_recognition
  - dlib (wheel spécifique pour Python 3.11)
  
Notes importantes :
------------------
- La wheel de dlib a été téléchargée pour Python 3.11 afin d'éviter les problèmes de compilation.
- Les images des visages à reconnaître doivent être placées dans le dossier "data".
- Pour exécuter le script de capture de photos : CaptureFace.py
- Pour exécuter le script de reconnaissance : Reconnaissance.py
