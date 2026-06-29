
 🎓 Student Placement Intelligence System

 📌 Project Overview
This is an AI-based web application that predicts whether a student will get placed or not based on academic performance and skill parameters like CGPA, Projects, Internships, Aptitude, and Communication skills.

The system uses Machine Learning (Random Forest Classifier) to analyze student data and give predictions with probability scores.

---

 🚀 How it Works

1. User enters student details:
   - CGPA
   - Number of Projects
   - Internships completed
   - Aptitude score
   - Communication skills score

2. Machine Learning model processes the input.

3. The model predicts:
   - ✅ Placed
   - ❌ Not Placed

4. It also shows:
   - Placement probability %
   - Feature importance graph

---

🧠 Machine Learning Model Used
- Algorithm: Random Forest Classifier
- Library: Scikit-learn
- Training: 80% data
- Testing: 20% data

---

 📊 Features
- Simple UI using Streamlit
- Real-time prediction
- Probability score output
- Feature importance visualization
- Student performance recommendations

---

 🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- Scikit-learn
- Matplotlib
---
👉 [Click Here to Open Live App]https://dhanu123-n-placement-intelligence-system-app-k3y4cy.streamlit.app/

 📁 Project Structure
 Student-Placement-Intelligence-System/
│
├── app.py
│   → Main Streamlit web application (UI + prediction)
│
├── model.pkl
│   → Trained Machine Learning model (Random Forest)
│
├── train_model.py
│   → Script used to train and save the ML model
│
├── dataset.csv
│   → Student dataset used for training/testing
│
├── requirements.txt
│   → List of required Python libraries
│
├── utils.py
│   → Helper functions (preprocessing, prediction, etc.)
│
├── visualization.py
│   → Feature importance graphs and charts
│
├── README.md
│   → Project documentation
│
└── assets/
    ├── logo.png
    └── screenshots/
        ├── home.png
        ├── prediction.png
        └── result.png
