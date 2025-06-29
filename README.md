# 🏦 Loan Prediction App

A Machine Learning-powered web application built with **Streamlit** that predicts whether a loan will be approved or not based on user inputs. The model is trained on historical loan application data using SVM.

🔗 [Live Demo](https://loan-prediction-app-jfpyxgadua4y5pxwqjtl9g.streamlit.app/) <!-- (update with your actual Streamlit Cloud link) -->

---
📊 Dataset Overview

The dataset used is a publicly available Loan Prediction Dataset containing information such as:

1.Gender, Marital Status, Dependents

2.Education, Employment Status

3.Applicant & Coapplicant Income

4.Loan Amount, Loan Term, Credit History

5.Property Area

Target: Loan Status (Y for approved, N for not approved)

🔗 Dataset Source: https://www.kaggle.com/datasets/ninzaami/loan-predication

##🎯 Skills Demonstrated:

1.Data cleaning & preprocessing

2.Data visualization for EDA

3.Handling categorical features

4.Machine learning model development

5.Model evaluation using accuracy

6.Understanding of SVM classifiers

## 📌 Features

- ✅ User-friendly web interface built with Streamlit
- 📊 Takes user inputs like income, education, credit history, etc.
- 🧠 Predicts loan approval using a trained Logistic Regression model
- 💾 Model and accuracy files saved using `pickle`
- 🔍 Clean and maintainable codebase

---

## 🚀 Tech Stack

 Tool      --        Purpose                          
 Python    --        Programming Language             
 Pandas, NumPy  --   Data manipulation & preprocessing
 Scikit-learn --      Model training                   
 Streamlit   --      Web app interface               
 Pickle       --     Model serialization              

---

## 📁 Project Structure

loan-prediction-app/
│
├── app.py # Streamlit web app
├── loan_model.sav # Trained ML model
├── requirements.txt # Required Python packages
├── loan_pred_accuracy.ipynb # Training and evaluation notebook




---

## 🛠️ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/AditiMishra2003/loan-prediction-app.git
   cd loan-prediction-app

2.Install Requirements
 ```bash
    pip install -r requirements.txt



```
🌱 Future Scope and Improvements:

1.Feature Engineering:
Derive new features such as income-to-loan ratio, total family income, etc., to enhance model performance.

2.Hyperparameter Tuning:
Use techniques like Grid Search or Randomized Search to find the best hyperparameters for the SVM model.

3.Use of Advanced Models:
Try ensemble models like Random Forest, XGBoost, or LightGBM for better prediction accuracy.

4.Cross-Validation:
Use K-Fold cross-validation for robust evaluation rather than a single train-test split.

5.Handle Missing Values Intelligently:
Instead of dropping rows, use imputation techniques (mean, median, or model-based).






