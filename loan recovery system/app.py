import streamlit as st
import pandas as pd
import pickle


with open('rf_model.pkl', 'rb') as file:
   model = pickle.load(file)

# Define the strategy logic
def assign_recovery_strategy(risk_score):
    if risk_score > 0.75:
        return "Immediate legal notices & aggressive recovery attempts"
    elif 0.50 <= risk_score <= 0.75:
        return "Settlement offers & repayment plans"
    else:
        return "Automated reminders & monitoring"

# Streamlit app
st.title("Loan Recovery Risk Predictor")

st.markdown("Enter new customer details below:")

# User input form
age = st.number_input("Age", 18, 100, 42)
income = st.number_input("Monthly Income", 0, 1000000, 55000)
loan_amt = st.number_input("Loan Amount", 0, 10000000, 150000)
tenure = st.number_input("Loan Tenure (months)", 1, 360, 60)
interest = st.number_input("Interest Rate (%)", 0.0, 30.0, 9.5)
collateral = st.number_input("Collateral Value", 0, 10000000, 200000)
outstanding = st.number_input("Outstanding Loan Amount", 0, 10000000, 80000)
emi = st.number_input("Monthly EMI", 0, 1000000, 3000)
missed = st.number_input("Missed Payments", 0, 50, 2)
dpd = st.number_input("Days Past Due", 0, 365, 15)

# Prediction button
if st.button("Predict Risk & Strategy"):
    new_customer = {
        'Age': age,
        'Monthly_Income': income,
        'Loan_Amount': loan_amt,
        'Loan_Tenure': tenure,
        'Interest_Rate': interest,
        'Collateral_Value': collateral,
        'Outstanding_Loan_Amount': outstanding,
        'Monthly_EMI': emi,
        'Num_Missed_Payments': missed,
        'Days_Past_Due': dpd
    }

    new_df = pd.DataFrame([new_customer])

    predicted_flag = model.predict(new_df)[0]
    risk_score = model.predict_proba(new_df)[0][1]

    strategy = assign_recovery_strategy(risk_score)

    st.subheader("Prediction Results")
    st.write("**High Risk:**", "Yes" if predicted_flag == 1 else "No")
    st.write(f"**Risk Score:** { risk_score:.2%}")
    st.write("**Recommended Recovery Strategy:**")
    st.success(strategy)
