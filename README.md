# 🎓 Student Performance Predictor

A **Machine Learning web application** that predicts a student’s **final grade (G3)** based on academic and background factors.  
Built using **Python, Scikit-learn, and Streamlit**, and deployed as an interactive web app.

---

## 🚀 Project Overview

The **Student Performance Predictor** uses a **Random Forest Regressor** to estimate a student’s final grade (**G3**) using historical academic data.

The model considers multiple factors such as:

- Student demographics  
- Family education background  
- Study habits  
- Academic history  

This project demonstrates a **complete end-to-end Machine Learning workflow**:

> **Exploratory Data Analysis → Model Training → Evaluation → Deployment via Streamlit**

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Regressor  
- **Problem Type:** Regression  
- **Target Variable:** Final Grade (**G3**)  

### 🔹 Features Used
- Age  
- Mother’s Education (**Medu**)  
- Father’s Education (**Fedu**)  
- Weekly Study Time  
- Number of Past Failures  
- Number of Absences  
- First Period Grade (**G1**)  
- Second Period Grade (**G2**)  

The trained model is saved and reused inside the Streamlit app to ensure fast and efficient predictions.

---

## 📈 Model Performance

The model was evaluated on a test dataset using standard regression metrics:

- **Mean Absolute Error (MAE):** <add your value>  
- **Root Mean Squared Error (RMSE):** <add your value>  
- **R² Score:** <add your value>  

> These metrics indicate how closely the predicted grades match the actual student grades.

---

## 🖥️ Web Application (Streamlit)

The Streamlit web app allows users to:

- Enter student details using interactive sliders  
- Get real-time predictions of final grades  
- Understand how machine learning can be applied in education  

### ✨ App Features
- Clean and beginner-friendly user interface  
- Interactive input controls  
- Instant prediction results  
- Lightweight and fast execution  

---

## 🚀 Live Demo

👉 **Streamlit App:**  
https://student-performance-predictor-f8jbrkrtcjq2waykkshq9n.streamlit.app
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

**Muskaan Manwanii**
B.Tech Student | Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it motivates me to build more!
