# Fraudulent Transaction Detection

This project builds a machine learning model to detect fraudulent credit card transactions. Using a real-world dataset, the model is trained to distinguish between legitimate and fraudulent activities, a critical task for financial security.

The analysis, feature engineering, and modeling process are all contained in the `fraudulent-transaction-detection.ipynb` notebook.

## 📊 Project Workflow

The project follows a standard machine learning pipeline:

1.  **Data Loading:** The model is trained on `fraudTrain.csv` and evaluated on `fraudTest.csv`.
2.  **Exploratory Data Analysis (EDA):**
    * Initial analysis showed **no missing values**.
    * Visualization of the target variable (`is_fraud`) revealed a **highly imbalanced dataset**, with fraudulent transactions representing a very small minority (less than 1%).
    * A correlation heatmap was generated to understand initial relationships between features.
3.  **Feature Engineering:**
    * **Temporal Features:** Extracted `hour`, `day`, `month`, and `day_of_week` from the `trans_date_trans_time` column, as the time of a transaction is a critical predictor.
    * **Encoding:** Categorical features (like `merchant`, `category`, `gender`, `job`) were converted to numerical values using `LabelEncoder`.
    * **Scaling:** All numerical features were scaled using `StandardScaler` to ensure the model isn't biased by features with different ranges.
    * **Feature Dropping:** Irrelevant or redundant columns (`Unnamed: 0`, `trans_num`, `unix_time`, `first`, `last`, etc.) were removed.
4.  **Modeling:**
    * An **XGBoost Classifier** (`XGBClassifier`) was chosen for its high performance and efficiency, especially with imbalanced datasets.
    * The model was trained on the processed `X_train` data with the following parameters: `n_estimators=300`, `max_depth=30`, `learning_rate=0.005`.
5.  **Evaluation:**
    * The model's performance was validated on the unseen `X_test` data.
    * A confusion matrix and classification report were generated to assess accuracy, precision, and recall.
6.  **Analysis & Output:**
    * Feature importance was extracted from the trained model.
    * All transactions from the test set that were *predicted* as fraudulent were saved to `predicted_fraud_records.csv`.
    * Visualizations were created for the predicted fraud, showing the top merchants and the distribution of fraudulent amounts.

## 📈 Results & Key Insights

The model performed exceptionally well, achieving a high overall accuracy while demonstrating a strong ability to identify the rare fraudulent class.

* **Overall Accuracy:** **99.88%**

### Performance on Fraud Class (1)

For fraud detection, precision and recall are more important than overall accuracy.

* **Precision:** **0.96**
    * *Interpretation:* When the model predicts a transaction is fraudulent, it is correct 96% of the time.
* **Recall:** **0.72**
    * *Interpretation:* The model successfully identifies 72% of all actual fraudulent transactions.
* **F1-Score:** **0.82**

### Feature Importance

The model identified the following as the most significant predictors of fraud:

1.  **`amt`**: The monetary value of the transaction.
2.  **`hour`**: The hour of the day the transaction occurred.
3.  **`category`**: The spending category (e.g., `shopping_net`, `misc_net`).


## 🛠️ Technologies Used

* **Data Manipulation:** `pandas`, `numpy`
* **Data Visualization:** `matplotlib`, `seaborn`
* **Machine Learning:** `scikit-learn` (for preprocessing and metrics)
* **Modeling:** `xgboost`

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn xgboost
    ```

3.  **Run the notebook:**
    Open and run the `fraudulent-transaction-detection.ipynb` notebook in Jupyter or any compatible environment.
