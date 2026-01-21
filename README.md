# 🎓 Student Performance Predictor

A Machine Learning web application that predicts a student's **final grade (G3)** based on academic and background factors.
Built using **Python, Scikit-learn, and Streamlit**.

---

## 🚀 Project Overview

The **Student Performance Predictor** uses a **Random Forest Regressor** model to estimate a student’s final grade (G3).
The model is trained on historical student performance data and considers factors such as:

* Age
* Parents' education
* Weekly study time
* Past failures
* Absences
* First & second period grades (G1, G2)

This project demonstrates the **end-to-end Machine Learning workflow**:

> Data analysis → Model training → Model deployment via web app

---

## 🧠 Machine Learning Model

* **Algorithm:** Random Forest Regressor
* **Target Variable:** Final Grade (G3)
* **Features Used:**

  * Age
  * Mother’s Education (Medu)
  * Father’s Education (Fedu)
  * Weekly Study Time
  * Past Class Failures
  * Number of Absences
  * First Period Grade (G1)
  * Second Period Grade (G2)

The model is trained inside the Streamlit app and cached for performance.

---

## 🖥️ Web Application (Streamlit)

The Streamlit app provides:

* Interactive sliders for student inputs
* Real-time grade prediction
* Clean and user-friendly interface

### App Features

* Simple UI with sliders
* Instant prediction on button click
* Informational message explaining the ML usage

---

## 📂 Project Structure

```
student-performance-predictor/
│
├── app.py                      # Streamlit web app
├── train_model.py              # Model training script
├── eda.ipynb                   # Exploratory Data Analysis
├── student-mat.csv             # Dataset
├── student_performance_model.pkl  # Trained ML model
├── requirements.txt            # Dependencies
├── .gitignore                  # Ignored files
└── README.md                   # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📊 Dataset

* Dataset: `student-mat.csv`
* Contains student academic and demographic data
* Commonly used for educational performance analysis

---

## 📌 Key Learnings

* Data preprocessing and feature selection
* Training and evaluating a regression model
* Model deployment using Streamlit
* Git & GitHub workflow
* Handling real-world ML project structure

---

## 🔮 Future Improvements

* Add model evaluation metrics (R², MAE)
* Include feature importance visualization
* Support multiple datasets
* Improve UI with charts
* Add model comparison (Linear Regression, XGBoost)

---

## 👩‍💻 Author

**Muskaan Manwani**
B.Tech Student | Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it motivates me to build more!
