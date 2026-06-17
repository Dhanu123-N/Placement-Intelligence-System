import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("🎓 Student Placement Intelligence System")

# Load Dataset
data = pd.read_csv("placement_dataset.csv")

# Convert Yes/No to 1/0
data["Placed"] = data["Placed"].map({"Yes": 1, "No": 0})

# Features and Target
X = data[["CGPA", "Projects", "Internships", "Aptitude", "Communication"]]
y = data["Placed"]

# Train Model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
st.info(f"🎯 Model Accuracy: {round(accuracy*100, 2)}%")

# Inputs
cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)
projects = st.number_input("Projects", 0, 10, 2)
internships = st.number_input("Internships", 0, 10, 1)
aptitude = st.number_input("Aptitude Score", 0, 100, 70)
communication = st.number_input("Communication Score", 0, 10, 7)

if st.button("Predict Placement"):

    student = pd.DataFrame({
        "CGPA": [cgpa],
        "Projects": [projects],
        "Internships": [internships],
        "Aptitude": [aptitude],
        "Communication": [communication]
    })

    prediction = model.predict(student)
    probability = model.predict_proba(student)

    st.subheader("📋 Result")

    if prediction[0] == 1:
        st.success("✅ Placement Prediction: YES")
    else:
        st.error("❌ Placement Prediction: NO")

    st.info(f"📊 Placement Probability: {round(max(probability[0]) * 100, 2)}%")

    # Recommendations
    st.subheader("🤖 AI Recommendations")

    if cgpa < 7:
        st.warning("Improve your CGPA above 7.0")

    if projects < 2:
        st.warning("Try to complete more projects")

    if internships < 1:
        st.warning("Complete at least one internship")

    if aptitude < 75:
        st.warning("Practice aptitude daily")

    if communication < 7:
        st.warning("Improve communication skills")

    # Feature Importance
    st.subheader("📊 Feature Importance")

    importance = model.feature_importances_
    features = X.columns

    fig, ax = plt.subplots()
    ax.barh(features, importance)   # FIXED (better view)
    st.pyplot(fig)