import cv2
import os

# ==============================
# CONFIGURATION
# ==============================

NAME = "Candra"
DATASET_DIR = "faces"

# Buat folder faces jika belum ada
os.makedirs(DATASET_DIR, exist_ok=True)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Webcam tidak dapat dibuka.")
    exit()

print(f"Registrasi wajah untuk: {NAME}")
print("Arahkan wajah ke kamera.")
print("Tekan Q untuk membatalkan.")

count = 0

while True:
    success, frame = camera.read()

    if not success:
        print("Gagal membaca frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        # Gambar kotak wajah
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Ambil area wajah
        face = gray[y:y+h, x:x+w]

        # Simpan gambar
        filename = os.path.join(
            DATASET_DIR,
            f"{NAME}_{count}.jpg"
        )

        cv2.imwrite(filename, face)

        count += 1

        cv2.putText(
            frame,
            f"Captured: {count}/30",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("FaceGate - Register", frame)

    # Berhenti setelah 30 gambar
    if count >= 30:
        break

    # Q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print()
print("Registrasi selesai.")
print(f"Total gambar: {count}")