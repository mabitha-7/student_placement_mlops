import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("saved_models/placement_model.pkl")

st.title("🎓 Student Placement Prediction App")

# Input fields
cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
major_projects = st.selectbox("Major Projects", [0, 1])
certificates = st.slider("Workshops/Certifications", 0, 5, 1)
mini_projects = st.slider("Mini Projects", 0, 5, 1)
skills = st.slider("Skills (0–10)", 0, 10, 5)
communication = st.slider("Communication Skill Rating", 0.0, 5.0, 3.0)
internship = st.selectbox("Internship", ["No", "Yes"])
hackathon = st.selectbox("Hackathon Participation", ["No", "Yes"])
hsc = st.slider("12th Percentage", 30, 100, 70)
ssc = st.slider("10th Percentage", 30, 100, 75)
backlogs = st.slider("Backlogs", 0, 10, 0)

# Convert categorical
internship = 1 if internship == "Yes" else 0
hackathon = 1 if hackathon == "Yes" else 0

# Prepare input
input_data = np.array([[cgpa, major_projects, certificates, mini_projects, skills,
                        communication, internship, hackathon, hsc, ssc, backlogs]])

# Predict
if st.button("Predict Placement Status"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ Student is Likely to be Placed")
    else:
        st.error("❌ Student is Likely Not to be Placed")
