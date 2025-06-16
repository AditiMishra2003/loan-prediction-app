# 🏦 Loan Prediction App

A Machine Learning-powered web application built with **Streamlit** that predicts whether a loan will be approved or not based on user inputs. The model is trained on historical loan application data using logistic regression.

🔗 [Live Demo](https://loan-prediction-app-jfpyxgadua4y5pxwqjtl9g.streamlit.app/) <!-- (update with your actual Streamlit Cloud link) -->

---
📊 Dataset Overview
The dataset used is a publicly available Loan Prediction Dataset containing information such as:

Gender, Marital Status, Dependents

Education, Employment Status

Applicant & Coapplicant Income

Loan Amount, Loan Term, Credit History

Property Area

Target: Loan Status (Y for approved, N for not approved)

🔗 Dataset Source: https://www.kaggle.com/datasets/ninzaami/loan-predication

## 📌 Features

- ✅ User-friendly web interface built with Streamlit
- 📊 Takes user inputs like income, education, credit history, etc.
- 🧠 Predicts loan approval using a trained Logistic Regression model
- 💾 Model and accuracy files saved using `pickle`
- 🔍 Clean and maintainable codebase

---

## 🚀 Tech Stack

 Tool              Purpose                          
 Python            Programming Language             
 Pandas, NumPy     Data manipulation & preprocessing
 Scikit-learn      Model training                   
 Streamlit         Web app interface               
 Pickle            Model serialization              

---

## 📁 Project Structure

loan-prediction-app/

── app.py # Streamlit web app
── loan_model.sav # Trained ML model
── requirements.txt # Required Python packages
── loan_pred_accuracy.ipynb # Training and evaluation notebook

yaml
Copy
Edit


---

## 🛠️ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/AditiMishra2003/loan-prediction-app.git
   cd loan-prediction-app
   Install dependencies:

2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

3. Run app.py
 streamlit run app.py

---
🌱 Future Scope and Improvements:
Feature Engineering:
Derive new features such as income-to-loan ratio, total family income, etc., to enhance model performance.

Hyperparameter Tuning:
Use techniques like Grid Search or Randomized Search to find the best hyperparameters for the SVM model.

Use of Advanced Models:
Try ensemble models like Random Forest, XGBoost, or LightGBM for better prediction accuracy.

Cross-Validation:
Use K-Fold cross-validation for robust evaluation rather than a single train-test split.

Handle Missing Values Intelligently:
Instead of dropping rows, use imputation techniques (mean, median, or model-based).

Deploy as Web Application:
Create a simple Flask or Streamlit app for loan officers to input data and get real-time predictions.

Fairness & Bias Analysis:
Ensure the model is fair and does not discriminate based on gender, property area, etc.





