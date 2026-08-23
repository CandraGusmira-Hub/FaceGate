# 🔐 FaceGate

**FaceGate** adalah aplikasi **Face Authentication System** berbasis Python yang menggunakan webcam dan facial recognition untuk melakukan autentikasi pengguna sebelum memberikan akses ke halaman dashboard.

Project ini dibuat sebagai project pembelajaran dan portfolio untuk mempelajari **Computer Vision, Face Recognition, Web Authentication, dan Flask Web Application**.

---

## 📖 Overview

FaceGate memungkinkan pengguna melakukan autentikasi menggunakan wajah yang telah terdaftar.

Berbeda dengan sistem login tradisional yang menggunakan username dan password, FaceGate menggunakan **facial recognition** untuk memverifikasi identitas pengguna.

### Cara kerja secara sederhana:

```text
Webcam
   ↓
Face Detection
   ↓
Face Recognition
   ↓
Identity Verification
   ↓
┌───────────────┐
│               │
▼               ▼
Recognized    Unknown
│               │
▼               ▼
Access         Access
Granted        Denied
│
▼
Dashboard
```

---

# ✨ Features

- 🔐 Face Authentication
- 📷 Real-time Webcam
- 👤 Face Registration
- 🧠 Face Detection
- 🎯 Face Recognition
- 🧠 LBPH Face Recognizer
- 🌐 Flask Web Application
- 🔒 Protected Dashboard
- 📊 Authentication Status
- 🚪 Access Control
- 📱 Responsive Dashboard

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Backend & web server |
| OpenCV | Computer vision & image processing |
| OpenCV-Contrib | LBPH face recognition |
| NumPy | Numerical & image data processing |
| HTML5 | Web structure |
| CSS3 | User interface |
| JavaScript | Webcam & client-side interaction |

---

# 📂 Project Structure

```text
FaceGate/
│
├── faces/
│
├── model/
│
├── templates/
│   ├── login.html
│   └── dashboard.html
│
├── app.py
├── main.py
├── register.py
├── train.py
├── recognize.py
├── access.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File / Folder | Description |
|---|---|
| `app.py` | Main Flask application |
| `main.py` | Main/supporting Python script |
| `register.py` | Face registration and image capture |
| `train.py` | Training facial recognition model |
| `recognize.py` | Facial recognition process |
| `access.py` | Authentication/access control |
| `templates/` | HTML templates |
| `faces/` | Local facial training dataset |
| `model/` | Trained facial recognition model |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files excluded from Git |
| `README.md` | Project documentation |

---

# 🧠 Face Recognition

FaceGate currently uses **LBPH (Local Binary Patterns Histograms)** through OpenCV-Contrib for facial recognition.

The recognition process consists of three major stages.

## 1. Face Registration

The webcam captures several images of the user's face.

```text
Webcam
   ↓
Face Detection
   ↓
Face Capture
   ↓
Face Dataset
```

The captured images are stored locally and used as training data.

---

## 2. Model Training

The collected facial images are processed by the training script.

```text
Face Dataset
     ↓
LBPH Training
     ↓
Trained Model
     ↓
Model File
```

The resulting model is then used during authentication.

---

## 3. Face Authentication

When a user attempts to log in, the webcam captures the user's face.

```text
Camera Frame
     ↓
Face Detection
     ↓
Face Extraction
     ↓
LBPH Prediction
     ↓
Identity Verification
```

If the detected face matches a registered user, access is granted.

If the face is unknown, access is denied.

---

# 🔄 Authentication Flow

```text
┌───────────────────┐
│   Open FaceGate   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  Allow Webcam     │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│    Scan Face      │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  Face Detection   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Face Recognition  │
└─────────┬─────────┘
          │
     ┌────┴────┐
     │         │
     ▼         ▼
   MATCH     UNKNOWN
     │         │
     ▼         ▼
  GRANTED    DENIED
     │
     ▼
┌───────────────────┐
│     Dashboard     │
└───────────────────┘
```

---

# ⚙️ Installation

## Requirements

Before running FaceGate, make sure you have:

- Python 3.13 or compatible version
- Git
- Working webcam
- Modern web browser
- Windows, Linux, or macOS

---

## 1. Clone Repository

```bash
git clone https://github.com/CandraGusmira-Hub/FaceGate.git
```

Enter the project directory:

```bash
cd FaceGate
```

---

## 2. Create Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

### Windows PowerShell

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, your terminal should look similar to:

```text
(venv) PS C:\...\FaceGate>
```

---

## 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

Main dependencies:

```text
Flask
OpenCV-Contrib-Python
NumPy
```

---

# ▶️ Running FaceGate

Start the Flask application:

```bash
python app.py
```

If the application starts successfully, the terminal will display:

```text
* Running on http://127.0.0.1:5000
```

Open your browser:

```text
http://127.0.0.1:5000
```

Allow webcam access when requested.

---

# 👤 Face Registration

Before authentication can be performed, a user's face needs to be registered.

Run:

```bash
python register.py
```

The application will capture facial images from the webcam.

The images are then stored locally as training data.

---

# 🧠 Train the Face Model

After registering a face, train the facial recognition model:

```bash
python train.py
```

The training process will generate the facial recognition model.

The model is stored locally inside:

```text
model/
```

---

# 🔐 Face Authentication

After the face has been registered and trained, run:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

The user can perform facial authentication through the webcam.

### Successful authentication:

```text
Face Detected
      ↓
Face Recognized
      ↓
Identity Verified
      ↓
Access Granted
      ↓
Dashboard
```

### Failed authentication:

```text
Face Detected
      ↓
Face Not Recognized
      ↓
Access Denied
```

---

# 🖥️ Dashboard

After successful authentication, the user can access the protected dashboard.

The dashboard is designed to provide information such as:

- Authentication status
- Security status
- User information
- Recent authentication activity
- System status
- Logout functionality

---

# 🔒 Security Considerations

FaceGate is currently a **learning and portfolio project** and should not be considered a production-ready biometric authentication system.

Important considerations:

- Facial data should be handled carefully.
- Facial datasets should not be uploaded to a public repository.
- Passwords, API keys, and other secrets should never be committed.
- LBPH recognition can be affected by lighting and camera quality.
- Facial recognition accuracy can vary depending on the training dataset.
- The current implementation does not provide advanced liveness detection.
- Additional security mechanisms should be implemented for production environments.

---

# 🚫 Git & Sensitive Files

The project uses `.gitignore` to prevent unnecessary or sensitive files from being uploaded.

Examples:

```text
venv/
.venv/
__pycache__/
.env
faces/
model/
.vscode/
```

Facial datasets and trained models should remain local unless there is a specific reason to distribute them.

---

# 🚧 Future Development

Planned improvements:

- [ ] Multi-user authentication
- [ ] User management
- [ ] Authentication history
- [ ] Database integration
- [ ] PostgreSQL support
- [ ] Admin dashboard
- [ ] Improved face recognition
- [ ] Liveness detection
- [ ] Anti-spoofing protection
- [ ] Better authentication security
- [ ] API integration
- [ ] Docker support
- [ ] Production deployment

---

# 📚 Learning Objectives

This project was developed to practice:

- Python programming
- Virtual environments
- Computer Vision
- Face Detection
- Face Recognition
- OpenCV
- OpenCV-Contrib
- LBPH
- Flask
- HTML & CSS
- JavaScript
- Webcam integration
- Web authentication
- Access control
- Git
- GitHub
- Project documentation

---

# 🧪 Project Status

**Status: 🟢 Functional Prototype**

Current functionality includes:

- ✅ Face registration
- ✅ Face dataset creation
- ✅ Face model training
- ✅ Face recognition
- ✅ Webcam integration
- ✅ Flask web application
- ✅ Facial authentication
- ✅ Protected dashboard
- ✅ Access control

---

# 📸 Screenshots

Screenshots can be added here to demonstrate the application interface.

Example:

```markdown
![Login Page](screenshots/login.png)

![Dashboard](screenshots/dashboard.png)
```

---

# 👨‍💻 Author

## Candra Gusmira

**Informatics Engineering Student**

Interested in:

- Software Development
- Web Development
- Computer Vision
- Python
- Backend Development
- Computer Technology

---

# 📄 License

This project is created for educational and portfolio purposes.

Feel free to study, modify, and improve the project for learning purposes.

---

# ⭐ Acknowledgements

FaceGate is built using several open-source technologies:

- Python
- Flask
- OpenCV
- OpenCV-Contrib
- NumPy

---

## ⭐ Support

If you find this project interesting, feel free to explore the source code and improve it.

**FaceGate — Face Authentication System built with Python & OpenCV. 🔐**