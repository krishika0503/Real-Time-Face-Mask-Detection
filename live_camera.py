import cv2
import numpy as np

# Load face detector
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Open camera
cap = cv2.VideoCapture(0)

# Check camera
if not cap.isOpened():
    print("Camera not opening")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Fix mirror view
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5
    )

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        # Lower half of face
        lower_face = face[int(h/2):h, :]

        mean_intensity = np.mean(lower_face)

        if mean_intensity < 100:
            label = "MASK"
            color = (0, 255, 0)
        else:
            label = "NO MASK"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(
            frame,
            label,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            color,
            2
        )

    cv2.imshow("Face Mask Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

