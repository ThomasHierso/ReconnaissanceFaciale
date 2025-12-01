import cv2, os 

# path du dossier où les photos seront enregistrées
save_path = r"C:\Users\thoma\Desktop\Code\Formation\ReconnaissanceFace\data"
os.makedirs(save_path, exist_ok=True)

# Initialisation du compteur de photos
num = 1

# Initialisation de la caméra par défaut 

video_capture = cv2.VideoCapture(0)  
while True:
    ret, frame = video_capture.read()
    # Dans le cas où la caméra ne fonctionne pas (vu que Ret booléen, on met If not)
    if not ret:
        print("Erreur capture webcam")
        break

    # Rajout d'une fonctionnalité pour inverser gauche droite (1 horizontal, 0 vertical) --> effet mirroir 
    frame = cv2.flip(frame,1)

    # Affichage
    cv2.imshow("Camera",frame)

    # permettre la lecture de la touche 
    key = cv2.waitKey(1) & 0xFF

    # Tprendre une photo avec c
    if key == ord('c'):
        filename = os.path.join(save_path, f"Thomas{num}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Photo {num} sauvegardée : {filename}")
        num += 1

    # fermeture de la fenetre par la touche q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# on ferme tout 
video_capture.release()
cv2.destroyAllWindows()
 
