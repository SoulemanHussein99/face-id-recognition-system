# Face ID Authentication System (OpenCV + Python)

A real-time face authentication system built using Python, OpenCV, and the face_recognition library.  
The system allows face enrollment and later verifies identity using facial encoding comparison.

---

## Features

- Real-time face detection using webcam
- Face enrollment (save face encoding locally)
- Face verification using face distance comparison
- Simple biometric-style authentication logic
- Visual bounding box around detected faces
- Keyboard-controlled operations

---

## Controls

- `S` → Save / Register current face (enrollment)
- `C` → Compare face with stored encoding (authentication)
- `Q` → Quit application

---

## Technologies Used

- Python 
- OpenCV (cv2)
- face_recognition library
- Haar Cascade Classifier
- Pickle (for saving face encoding)

---

## How It Works

1. Webcam captures live video frames  
2. Face is detected in real-time  
3. If user presses `S`, face encoding is saved locally  
4. On pressing `C`, current face is compared with saved encoding  
5. If similarity threshold is met → **Match**  
6. Otherwise → **No Match**
