import streamlit as st
import joblib

# Load trained model
model = joblib.load("student_model.pkl")

# App title
st.title("🎓 Student Grades Prediction")

st.write("Enter student details to predict the Exam Score.")

# Student inputs
hours_studied = st.number_input(
    "Hours Studied",
    min_value=0,
    max_value=24,
    value=5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

previous_scores = st.number_input(
    "Previous Scores",
    min_value=0,
    max_value=100,
    value=60
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0,
    max_value=24,
    value=7
)

tutoring_sessions = st.number_input(
    "Tutoring Sessions",
    min_value=0,
    max_value=20,
    value=2
)

physical_activity = st.number_input(
    "Physical Activity",
    min_value=0,
    max_value=10,
    value=5
)

# Prediction button
if st.button("Predict Exam Score"):

    st.write("Prediction button clicked!")