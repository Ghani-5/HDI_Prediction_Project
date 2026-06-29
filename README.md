# 🌍 Human Development Index (HDI) Prediction

## 📌 Project Overview

This project predicts the **Human Development Group** of a country using Machine Learning. The prediction is based on four important development indicators:

- Life Expectancy at Birth
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) Per Capita

The application is built using **Python**, **Scikit-learn**, and **Flask**.

---

## 🚀 Technologies Used

- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib
- HTML
- CSS

---

## 📂 Dataset

The dataset contains Human Development data for different countries.

Features used:

- Life Expectancy at Birth (2021)
- Expected Years of Schooling (2021)
- Mean Years of Schooling (2021)
- Gross National Income Per Capita (2021)

Target:

- Human Development Groups
  - Low
  - Medium
  - High
  - Very High

## Live Website

https://hdi-prediction-project.onrender.com/

## Demo Video

https://drive.google.com/file/d/1XslzhMbz3xsZY69jkuh4jpzO8M3W1x6s/view?usp=sharing

## GitHub Repository

https://github.com/Ghani-5/HDI_Prediction_Project

📷 Sample Output
Input
Feature	                    :Value
--------------------------------------
Life Expectancy	            :82
Expected Years of Schooling	:18
Mean Years of Schooling	    :13
GNI Per Capita	            :60000

Prediction
Predicted HDI Group:
Very High

---

## 🤖 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Model Accuracy:

- **94.87%**

---

## 📁 Project Structure

```
HDI_PREDICTION_PROJECT/
│
├── app.py
├── train_model.py
├── model.pkl
├── encoder.pkl
├── requirements.txt
│
├── dataset/
│   └── hdi.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository

2. Install the required libraries

```
pip install -r requirements.txt
```

3. Run the Flask application

```
python app.py
```

4. Open your browser

```
https://hdi-prediction-project.onrender.com/
```

5. Enter the input values and click **Predict**.

---

## 📷 Output

The web application predicts one of the following categories:

- Low
- Medium
- High
- Very High

---

## 📌 Future Improvements

- Improve UI design
- Add graphical analysis
- Support multiple years of HDI data
- Deploy the application online

---

## 👨‍💻 Author

**SHAIK GHAN SAIDA**

Machine Learning Internship Project