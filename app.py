import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Predictor",
    layout="centered"
)

# ---------------- TITLE & INTRO ----------------
st.title("🎓 Student Performance Predictor")
st.write("Predict a student's final grade (G3) using Machine Learning")

st.info(
    "This app uses a Random Forest Regression model trained on historical student "
    "performance data to estimate the final grade (G3)."
)

# ---------------- LOAD DATA & TRAIN MODEL ----------------
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

    # Model evaluation
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))

    return model, features, X, y, y_pred, r2, mae, rmse

model, features, X, y, y_pred, r2, mae, rmse = train_model()

# ---------------- MODEL PERFORMANCE ----------------
st.subheader("📊 Model Performance")

col1, col2, col3 = st.columns(3)
col1.metric("R² Score", f"{r2:.3f}")
col2.metric("MAE", f"{mae:.2f}")
col3.metric("RMSE", f"{rmse:.2f}")

# ---------------- ACTUAL VS PREDICTED ----------------
st.subheader("📈 Actual vs Predicted Final Grades")

eval_df = pd.DataFrame({
    "Actual G3": y,
    "Predicted G3": y_pred
})

st.scatter_chart(eval_df)

# ---------------- FEATURE IMPORTANCE ----------------
st.subheader("📌 Feature Importance")

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

st.bar_chart(importance_df.set_index("Feature"))

# ---------------- USER INPUT ----------------
st.subheader("🧑‍🎓 Enter Student Details")

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
if st.button("🎯 Predict Final Grade"):
    prediction = model.predict(input_df)[0]
    prediction = max(0, min(20, round(prediction, 2)))

    st.success(f"Predicted Final Grade (G3): **{prediction} / 20**")
