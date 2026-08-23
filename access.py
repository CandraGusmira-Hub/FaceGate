import cv2
import webbrowser
import time

# ==============================
# CONFIGURATION
# ==============================

MODEL_PATH = "model/face_model.yml"

PERSON_ID = 1
PERSON_NAME = "Candra"

# Website yang akan dibuka
PROTECTED_URL = "https://www.google.com"

# Threshold recognition
CONFIDENCE_THRESHOLD = 70

# ==============================
# FACE DETECTOR
# ==============================

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# ==============================
# LOAD MODEL
# ==============================

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(MODEL_PATH)

print("FaceGate Access System")
print("======================")
print("Model berhasil dimuat.")
print("Tekan Q untuk keluar.")

# ==============================
# CAMERA
# ==============================

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Webcam tidak dapat dibuka.")
    exit()

# Mencegah browser dibuka berkali-kali
access_granted = False

while True:

    success, frame = camera.read()

    if not success:
        print("Gagal membaca frame.")
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face)

        # ==============================
        # FACE MATCH
        # ==============================

        if (
            label == PERSON_ID
            and confidence < CONFIDENCE_THRESHOLD
        ):

            name = PERSON_NAME
            status = "ACCESS GRANTED"
            box_color = (0, 255, 0)

            # ==============================
            # OPEN WEBSITE
            # ==============================

            if not access_granted:

                print()
                print("==============================")
                print("ACCESS GRANTED")
                print(f"Welcome, {PERSON_NAME}!")
                print("Opening protected page...")
                print("==============================")

                access_granted = True

                webbrowser.open(PROTECTED_URL)

                time.sleep(2)

        else:

            name = "Unknown"
            status = "ACCESS DENIED"
            box_color = (0, 0, 255)

        # ==============================
        # DRAW FACE
        # ==============================

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            box_color,
            2
        )

        cv2.putText(
            frame,
            name,
            (x, y - 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            box_color,
            2
        )

        cv2.putText(
            frame,
            status,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            box_color,
            2
        )

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
    # SHOW CAMERA
    # ==============================

    cv2.imshow(
        "FaceGate - Protected Access",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()