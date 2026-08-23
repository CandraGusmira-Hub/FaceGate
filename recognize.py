import cv2

# ==============================
# CONFIGURATION
# ==============================

MODEL_PATH = "model/face_model.yml"

# ID user
PERSON_ID = 1
PERSON_NAME = "Candra"

# ==============================
# LOAD FACE DETECTOR
# ==============================

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# ==============================
# LOAD TRAINED MODEL
# ==============================

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read(MODEL_PATH)

print("Face recognition model berhasil dimuat.")
print("Tekan Q untuk keluar.")

# ==============================
# OPEN WEBCAM
# ==============================

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Webcam tidak dapat dibuka.")
    exit()

while True:

    success, frame = camera.read()

    if not success:
        print("Gagal membaca frame.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    # ==============================
    # RECOGNIZE EVERY FACE
    # ==============================

    for (x, y, w, h) in faces:

        # Crop face
        face = gray[y:y+h, x:x+w]

        # Predict
        label, confidence = recognizer.predict(face)

        # LBPH confidence:
        # Semakin kecil = semakin mirip
        if label == PERSON_ID and confidence < 70:

            name = PERSON_NAME
            status = "ACCESS GRANTED"

            box_color = (0, 255, 0)

        else:

            name = "Unknown"
            status = "ACCESS DENIED"

            box_color = (0, 0, 255)

        # ==============================
        # DRAW FACE BOX
        # ==============================

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            box_color,
            2
        )

        # ==============================
        # DISPLAY NAME
        # ==============================

        cv2.putText(
            frame,
            name,
            (x, y - 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            box_color,
            2
        )

        # ==============================
        # DISPLAY STATUS
        # ==============================

        cv2.putText(
            frame,
            status,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            box_color,
            2
        )

        # ==============================
        # DISPLAY CONFIDENCE
        # ==============================

        cv2.putText(
            frame,
            f"Score: {confidence:.1f}",
            (x, y + h + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            box_color,
            2
        )

    # ==============================
    # DISPLAY CAMERA
    # ==============================

    cv2.imshow(
        "FaceGate - Face Recognition",
        frame
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ==============================
# CLEANUP
# ==============================

camera.release()
cv2.destroyAllWindows()