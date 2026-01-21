import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
df = pd.read_csv("student-mat.csv")

# Features used by the app
features = [
    "age", "Medu", "Fedu", "studytime",
    "failures", "absences", "G1", "G2"
]

X = df[features]
y = df["G3"]

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
model.fit(X, y)

# Save model
joblib.dump(model, "student_performance_model.pkl")

print("Model saved successfully!")
