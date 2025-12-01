import cv2
import face_recognition
import numpy as np
import os

# Charger les images de référence
images_path = r"C:\Users\thoma\Desktop\Code\Formation\ReconnaissanceFace\data"
known_face_encodings = []
known_face_names = []


for filename in os.listdir(images_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # chargement
        image = face_recognition.load_image_file(os.path.join(images_path,filename))  
        # encodage
        encoding = face_recognition.face_encodings(image)[0] 
        # on rajoute les photos encodés à la liste du visage qui doit être reconnu
        known_face_encodings.append(encoding)
        
        # on récup le nom du fichier sans extension
        base_name = os.path.splitext(filename)[0]  

        # Retirer les chiffres à la fin si présents
        name = ''.join([c for c in base_name if not c.isdigit()])  
        known_face_names.append(name)


# 2️⃣ Initialiser la caméra
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Erreur capture webcam")
        break

# On redimensionne pour plus d'efficacité 

    # 🔹 Redimensionner la frame pour accélérer la détection
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # 🔹 Détection sur la petite frame
    face_locations_small = face_recognition.face_locations(rgb_small_frame)
    face_encodings_small = face_recognition.face_encodings(rgb_small_frame, face_locations_small)

    # 🔹 Ajuster les coordonnées pour la frame originale
    face_locations = [(top*4, right*4, bottom*4, left*4) for (top, right, bottom, left) in face_locations_small]
    face_encodings = face_encodings_small    
    
    face_names = []
    for face_encoding in face_encodings:
        # comparaison visage
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding,tolerance=0.6)  # remplacer None par la comparaison
        name = "Inconnu"

        # application du nom si match
        if  True in matches:  
            idx=matches.index(True)
            name = known_face_names[idx]

        face_names.append(name)

    #  Affichage du rectangle et nom (vert s'il reconnait mon visage, rouge sinon)
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        color = (0, 255, 0) if name == "Thomas" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    cv2.imshow("Reconnaissance", frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
