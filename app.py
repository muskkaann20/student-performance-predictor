import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Performance Predictor",
    layout="centered"
)

# Load trained model
model = joblib.load("student_performance_model.pkl")

st.title("🎓 Student Performance Predictor")
st.write("Predict a student's final grade (G3) using machine learning")

# ---- USER INPUT FORM ----
st.header("Enter Student Details")

school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Sex", ["F", "M"])
age = st.slider("Age", 15, 22, 17)
address = st.selectbox("Address", ["U", "R"])
famsize = st.selectbox("Family Size", ["LE3", "GT3"])
Pstatus = st.selectbox("Parents Status", ["T", "A"])

Medu = st.slider("Mother's Education (0–4)", 0, 4, 2)
Fedu = st.slider("Father's Education (0–4)", 0, 4, 2)

studytime = st.slider("Weekly Study Time (1–4)", 1, 4, 2)
failures = st.slider("Past Class Failures", 0, 3, 0)
absences = st.slider("Number of Absences", 0, 93, 4)

G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

input_data = pd.DataFrame([{
    "school": school,
    "sex": sex,
    "age": age,
    "address": address,
    "famsize": famsize,
    "Pstatus": Pstatus,
    "Medu": Medu,
    "Fedu": Fedu,
    "studytime": studytime,
    "failures": failures,
    "absences": absences,
    "G1": G1,
    "G2": G2
}])

if st.button("Predict Final Grade"):
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Final Grade (G3): {prediction:.2f}")

