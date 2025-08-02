# 🛍️ Product Recommendation System using catboost 

This project contains a model that predicts whether a product should be recommended to a customer or not based on some defined features

---

## 📘 Project Overview

The notebook demonstrates:

- Loading and cleaning transactional retail data
- Feature engineering to generate relevant features for the model
- Building a classification model using catboost
- Visualizing important features
- interactive GUI build using ipywidgets 



---

## 📁 Files

- `product recommendation system.ipynb`: Jupyter Notebook with all code and outputs
- `Online-Retail.xlsx`: Raw transactional dataset (from a UK-based e-commerce store)


---

## 📊 Dataset Description

The dataset (`Online-Retail.xlsx`) includes one year of transactions from an online UK-based retailer. Key columns:

- `InvoiceNo`: Transaction ID
- `StockCode`: Item code
- `Description`: Item name
- `Quantity`: Units sold
- `InvoiceDate`: Date of transaction
- `UnitPrice`: Price per item
- `CustomerID`: Customer identifier
- `Country`: Customer’s country

---

## 🧹 Data Cleaning Steps

- Removed rows with missing `CustomerID`
- Filtered out negative quantities (likely returns)
- Converted data types for date and prices

---

## 📈 Analysis & Recommendation Logic

- **Top products**: Based on frequency of purchase
- **Top customers**: Based on total spending
- **product recommendation**: popular products recommended universally



---


