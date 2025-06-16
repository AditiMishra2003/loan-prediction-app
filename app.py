import pickle
import streamlit as st
import numpy as np

# Load the saved model
model = pickle.load(open('loan_model.sav', 'rb'))

# Title
st.title("Loan Status Prediction App")

# Input fields
Gender = st.selectbox('Gender', ['Male', 'Female'])
Married = st.selectbox('Married', ['Yes', 'No'])
Dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
Education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
Self_Employed = st.selectbox('Self Employed', ['Yes', 'No'])
ApplicantIncome = st.number_input('Applicant Income', min_value=0)
CoapplicantIncome = st.number_input('Coapplicant Income', min_value=0)
LoanAmount = st.number_input('Loan Amount (in thousands)', min_value=0)
Loan_Amount_Term = st.number_input('Loan Amount Term', min_value=0)
Credit_History = st.selectbox('Credit History', [1.0, 0.0])
Property_Area = st.selectbox('Property Area', ['Rural', 'Semiurban', 'Urban'])

# Convert inputs to model format
Gender = 1 if Gender == 'Male' else 0
Married = 1 if Married == 'Yes' else 0
Education = 1 if Education == 'Graduate' else 0
Self_Employed = 1 if Self_Employed == 'Yes' else 0
Dependents = 4 if Dependents == '3+' else int(Dependents)
Property_Area = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}[Property_Area]

input_data = np.array([[Gender, Married, Dependents, Education, Self_Employed,
                        ApplicantIncome, CoapplicantIncome, LoanAmount,
                        Loan_Amount_Term, Credit_History, Property_Area]])

# Prediction
if st.button("Predict Loan Status"):
    result = model.predict(input_data)
    if result[0] == 1:
        st.success("Congratulations! Loan will be Approved ✅")
    else:
        st.error("Sorry, Loan will not be Approved ❌")
