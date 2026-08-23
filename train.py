import cv2
import os
import glob
import numpy as np

DATASET_DIR = "faces"
MODEL_DIR = "model"

os.makedirs(MODEL_DIR, exist_ok=True)

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

PERSON_ID = 1

image_paths = glob.glob(
    os.path.join(DATASET_DIR, "*.jpg")
)

if not image_paths:
    print("Tidak ada dataset wajah di folder faces.")
    exit()

for image_path in image_paths:

    image = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    if image is None:
        continue

    faces.append(image)
    labels.append(PERSON_ID)

print(f"Dataset ditemukan: {len(faces)} gambar")
print("Training face recognition...")

recognizer.train(
    faces,
    np.array(labels)
)

model_path = os.path.join(
    MODEL_DIR,
    "face_model.yml"
)

recognizer.write(model_path)

print("Training selesai.")
print(f"Model disimpan di: {model_path}")