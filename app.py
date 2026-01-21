import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Predictor",
    layout="centered"
)

st.title("🎓 Student Performance Predictor")
st.write("Predict a student's final grade (G3) using Machine Learning")

# ---------------- TRAIN MODEL INSIDE APP ----------------
@st.cache_resource
def train_model():
    df = pd.read_csv("student-mat.csv")

    features = [
        "age", "Medu", "Fedu", "studytime",
        "failures", "absences", "G1", "G2"
    ]

    X = df[features]
    y = df["G3"]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
    model.fit(X, y)

    return model, features

model, features = train_model()

# ---------------- USER INPUT ----------------
st.header("Enter Student Details")

age = st.slider("Age", 15, 22, 17)
Medu = st.slider("Mother's Education (0–4)", 0, 4, 2)
Fedu = st.slider("Father's Education (0–4)", 0, 4, 2)
studytime = st.slider("Weekly Study Time (1–4)", 1, 4, 2)
failures = st.slider("Past Class Failures", 0, 3, 0)
absences = st.slider("Number of Absences", 0, 93, 4)
G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

input_df = pd.DataFrame([[
    age, Medu, Fedu, studytime,
    failures, absences, G1, G2
]], columns=features)

# ---------------- PREDICTION ----------------
if st.button("Predict Final Grade"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Final Grade (G3): {prediction:.2f}")
