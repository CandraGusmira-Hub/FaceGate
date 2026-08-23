from flask import Flask, render_template, request, jsonify, session, redirect
import cv2
import numpy as np
import base64
import os


# =====================================
# FLASK CONFIGURATION
# =====================================

app = Flask(__name__)

# Secret key untuk session
app.secret_key = "facegate-secret-key"


# =====================================
# FACE RECOGNITION CONFIGURATION
# =====================================

MODEL_PATH = "model/face_model.yml"

PERSON_ID = 1
PERSON_NAME = "Candra"

CONFIDENCE_THRESHOLD = 70


# =====================================
# LOAD FACE DETECTOR
# =====================================

face_cascade = cv2.CascadeClassifier(

    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"

)


# =====================================
# LOAD TRAINED MODEL
# =====================================

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read(MODEL_PATH)


# =====================================
# HOME / LOGIN
# =====================================

@app.route("/")
def home():

    # Kalau sudah login
    if session.get("authenticated"):

        return redirect("/dashboard")

    return render_template("login.html")


# =====================================
# FACE RECOGNITION API
# =====================================

@app.route("/recognize", methods=["POST"])
def recognize():

    try:

        # Ambil JSON
        data = request.get_json()

        image_data = data["image"]


        # ==============================
        # REMOVE BASE64 HEADER
        # ==============================

        image_data = image_data.split(",")[1]


        # ==============================
        # DECODE IMAGE
        # ==============================

        image_bytes = base64.b64decode(image_data)

        np_array = np.frombuffer(
            image_bytes,
            np.uint8
        )

        frame = cv2.imdecode(
            np_array,
            cv2.IMREAD_COLOR
        )


        # ==============================
        # GRAYSCALE
        # ==============================

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )


        # ==============================
        # DETECT FACE
        # ==============================

        faces = face_cascade.detectMultiScale(

            gray,

            scaleFactor=1.1,

            minNeighbors=5,

            minSize=(100, 100)

        )


        # Tidak ada wajah
        if len(faces) == 0:

            return jsonify({

                "success": False,

                "message": "No face detected"

            })


        # ==============================
        # RECOGNITION
        # ==============================

        for (x, y, w, h) in faces:

            face = gray[y:y+h, x:x+w]


            label, confidence = recognizer.predict(face)


            print(
                f"Label: {label} | "
                f"Confidence: {confidence:.2f}"
            )


            # ==============================
            # CHECK IDENTITY
            # ==============================

            if (

                label == PERSON_ID

                and confidence < CONFIDENCE_THRESHOLD

            ):

                # Login berhasil

                session["authenticated"] = True

                session["user"] = PERSON_NAME


                return jsonify({

                    "success": True,

                    "name": PERSON_NAME,

                    "confidence": confidence

                })


        # Tidak cocok

        return jsonify({

            "success": False,

            "message": "Face not recognized"

        })


    except Exception as error:

        print("Recognition error:", error)

        return jsonify({

            "success": False,

            "message": "Server error"

        }), 500


# =====================================
# DASHBOARD
# =====================================

@app.route("/dashboard")
def dashboard():

    # Cek authentication

    if not session.get("authenticated"):

        return redirect("/")


    return render_template(
        "dashboard.html",
        username=session.get("user")
    )


# =====================================
# LOGOUT
# =====================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =====================================
# RUN SERVER
# =====================================

if __name__ == "__main__":

    app.run(
        debug=True
    )