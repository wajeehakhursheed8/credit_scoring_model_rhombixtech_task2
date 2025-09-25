# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --- CONFIG ---
st.set_page_config(page_title="Credit Scoring App", layout="centered")

# --- LOAD MODEL ---
MODEL_PATH = os.path.join("models", "credit_model.pkl")
model = joblib.load(MODEL_PATH)

# --- APP TITLE ---
st.title(" Credit Scoring System")
st.write("Enter applicant details and get a prediction + credit score (0–1000).")

# --- USER INPUTS ---
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income", min_value=0, value=50000, step=1000)
loan_amount = st.number_input("Loan Amount", min_value=0, value=10000, step=500)
credit_history = st.selectbox(
    "Credit History", options=[1, 0],
    format_func=lambda x: "Good" if x == 1 else "Bad"
)
employment_status = st.selectbox(
    "Employment Status", options=[1, 0],
    format_func=lambda x: "Employed" if x == 1 else "Unemployed"
)
num_credit_cards = st.number_input("Number of Credit Cards", min_value=0, max_value=20, value=1)
defaulted_before = st.selectbox(
    "Defaulted Before", options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# --- PREDICTION ---
if st.button("Predict"):
    # Build DataFrame for input
    input_df = pd.DataFrame([{
        "Age": age,
        "Income": income,
        "LoanAmount": loan_amount,
        "CreditHistory": credit_history,
        "EmploymentStatus": employment_status,
        "NumCreditCards": num_credit_cards,
        "DefaultedBefore": defaulted_before
    }])

    # Predict
    pred = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]  # probability of being creditworthy
    score = int(proba * 1000)

    # Results
    st.subheader("Prediction")
    if pred == 1:
        st.success(" Creditworthy")
    else:
        st.error(" Not Creditworthy")

    st.metric(label="Credit Score (0–1000)", value=score, delta=f"{int(proba*100)}% prob")

    st.progress(min(max(proba, 0.0), 1.0))

    with st.expander("Input Summary"):
        st.write(input_df.T)

# --- OPTIONAL DATASET VISUALS ---
st.markdown("---")
st.subheader(" Dataset Insights (optional)")
if st.checkbox("Show dataset & visuals"):
    try:
        df = pd.read_csv("data/credit_data.csv")
        st.write(df.head())
        st.write("Creditworthy distribution:")
        st.bar_chart(df["Creditworthy"].value_counts())
    except FileNotFoundError:
        st.error("Dataset not found at data/credit_data.csv")
