import cv2

# Load face detector dari OpenCV
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Membuka webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Webcam tidak dapat dibuka.")
    exit()

print("FaceGate berjalan.")
print("Tekan Q untuk keluar.")

while True:
    success, frame = camera.read()

    if not success:
        print("Gagal membaca frame.")
        break

    # Mengubah frame menjadi grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    # Menggambar kotak pada setiap wajah
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Face Detected",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    # Menampilkan jumlah wajah
    cv2.putText(
        frame,
        f"Faces: {len(faces)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    # Tampilkan kamera
    cv2.imshow("FaceGate - Face Detection", frame)

    # Tekan Q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()