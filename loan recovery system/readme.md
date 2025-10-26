# 🏦 Loan Recovery Prediction System

This repository contains a machine learning project that aims to predict the likelihood of loan recovery using various borrower and loan-related attributes. By analyzing past data, the system helps financial institutions estimate recovery outcomes and make better lending decisions.

## 📁 Project Contents

- `loan recovery system.ipynb` – Jupyter Notebook containing data analysis, preprocessing, model training, evaluation, and predictions.
- `loan-recovery.xlsx` – Dataset used for model training and evaluation.

## 📌 Problem Statement

Loan defaults pose a major risk to financial institutions. This project aims to build a predictive model that determines whether a loan is likely to be recovered or not based on available borrower and loan information.

## 🔍 Workflow Overview

1. **Data Exploration**
   - Inspect structure and distribution of data
   - Handle missing values and outliers (if any)

2. **Data Preprocessing**
   - Encode categorical variables
   - Feature scaling (if necessary)
   - Split data into train and test sets

3. **Model Training**
   - Use machine learning classifiers such as:
     - Logistic Regression
     - Random Forest
     - Decision Tree
   - Evaluate with accuracy, precision, recall, F1-score, etc.

4. **Prediction and Evaluation**
   - Compare models to determine the best performer
   - Visualize confusion matrix and ROC-AUC curves

## 🧠 Features Used 

> I have used 10 features for the prediction. Examples include:

- Loan Amount
- Term
- Interest Rate
- Borrower Risk Score (predicted output)
- Days past due
- Recovery Strategy (Target Variable)

## 🛠️ Technologies Used

- Python 3.x
- Jupyter Notebook
- Pandas
- Scikit-learn
- Plotly

## ✅ Future Enhancements
- Hyperparameter tuning with GridSearchCV or RandomizedSearchCV

- Add more borrower features

- Deploy as a web app using Streamlit or Flask
