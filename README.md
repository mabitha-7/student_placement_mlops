# 🎓 Student Placement Prediction using MLOps

## 📌 Project Overview

This project is a Machine Learning-based web application that predicts whether a student is likely to get placed or not based on academic performance and skills.

The project follows basic **MLOps practices**, including model training, saving, and deployment using Streamlit.

---

## 🚀 Features

* Predict student placement status (Placed / Not Placed)
* User-friendly web interface using Streamlit
* Machine Learning model with high accuracy (~94%)
* End-to-end pipeline (Data → Model → Deployment)

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## 📂 Project Structure

```
student_placement_mlops/
│
├── data/
│   └── placement.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── saved_models/
│   └── placement_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/student_placement_mlops.git
cd student_placement_mlops
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```
streamlit run app.py
```

---

## 🌐 Usage

* Enter student details like CGPA, skills, internships, etc.
* Click on **Predict Placement Status**
* The model will predict whether the student is likely to be placed

---

## 🧠 Machine Learning Model

* Algorithm: Random Forest Classifier
* Accuracy: ~94%
* Model saved using Joblib

---

## 📊 Future Improvements

* Add more features for better prediction
* Deploy using Docker
* Integrate CI/CD pipeline
* Create REST API using Flask/FastAPI

---

## 👩‍💻 Author

* Mabitha M

---

## ⭐ Acknowledgement

This project is created for learning Machine Learning and MLOps concepts.

---
