<<<<<<< HEAD
#Description how t run the project
# MLOPS
NEW REPO FOR RESEARCH MLOPS PROJECT
hello checking
=======
# 🩺 Diabetes Prediction System (FastAPI + Machine Learning)

## 📌 Project Description
This project is a Machine Learning-based Diabetes Prediction System built using Python, FastAPI, and Scikit-learn.  
It predicts whether a patient is diabetic or non-diabetic based on medical attributes like age, urea, creatinine, HbA1c, cholesterol, triglycerides, HDL, LDL, VLDL, BMI, and gender.

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repo-link>
cd assignment
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / WSL:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Run FastAPI Server

```bash
uvicorn app:app --reload
```

Server will run at:
http://localhost:8000

Swagger UI:
http://localhost:8000/docs

---

## 📡 Example cURL Requests

### ✔ Diabetic Prediction
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"AGE\":65,\"Urea\":7.5,\"Cr\":52.0,\"HbA1c\":11.2,\"Chol\":6.1,\"TG\":2.8,\"HDL\":0.9,\"LDL\":3.5,\"VLDL\":1.2,\"BMI\":32.5,\"Gender\":\"M\"}"
```

### ✔ Non-Diabetic Prediction
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"AGE\":28,\"Urea\":4.2,\"Cr\":48.0,\"HbA1c\":5.1,\"Chol\":4.0,\"TG\":1.2,\"HDL\":1.8,\"LDL\":2.1,\"VLDL\":0.6,\"BMI\":22.0,\"Gender\":\"F\"}"
```

### ❌ Invalid Gender Test
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"AGE\":45,\"Urea\":5.0,\"Cr\":50.0,\"HbA1c\":6.0,\"Chol\":5.0,\"TG\":1.5,\"HDL\":1.2,\"LDL\":2.5,\"VLDL\":0.8,\"BMI\":25.0,\"Gender\":\"X\"}"
```

---

## 📊 Model Performance

| Model                | Accuracy | Precision | Recall |
|---------------------|----------|-----------|--------|
| Logistic Regression | 92%      | 91%       | 90%    |
| Random Forest       | 96%      | 95%       | 94%    |

---

## 🧠 Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Uvicorn

---

## 📌 Features

- ML-based diabetes prediction
- REST API using FastAPI
- Input validation using Pydantic
- Gender validation
- cURL testing support

---

## 👨‍💻 Author

Student Project – Machine Learning + FastAPI Integration
>>>>>>> 4cc4efb (Update README with project documentation)
