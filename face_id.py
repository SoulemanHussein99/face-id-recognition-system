import cv2
import face_recognition
import pickle
import os    

clf = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_encodeing = None

camera = cv2.VideoCapture(0)

while True:
    k = cv2.waitKey(1)
    success, frame = camera.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encoding = face_recognition.face_encodings(rgb_frame)
    if len(encoding) > 0:
        current_face = encoding[0]
    faces = clf.detectMultiScale(rgb_frame, 1.1, 4, cv2.CASCADE_SCALE_IMAGE)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (125, 250, 0), 2)
    
    # for comparing the face on the video with the regisrered face 
    
    # checking if there is a face
    if face_encodeing is not None:
        dist = face_recognition.face_distance([face_encodeing], current_face)
        if k == ord("c"):
            if dist < 0.5:
                text = "Match"
                os.system("start cmd")
            else:
                text = "No Match"
                os.system("sleep 1")
            cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("face_id", frame)
    
    # start registering
    try:
        with open("face_encodeing", "rb") as f:
            face_encodeing = pickle.load(f)
    except:
        if k == ord("s"):
            if len(encoding) > 0:
                face_encodeing = encoding[0]
                with open("face_encodeing", "wb") as f:
                    pickle.dump(face_encodeing, f)

    if k == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()