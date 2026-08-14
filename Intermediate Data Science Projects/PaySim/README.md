# 💳 PaySim Fraud Detection

Exploratory Data Analysis (EDA), Feature Engineering, Class Imbalance Handling, and Machine Learning project using the PaySim mobile money transactions dataset. This project investigates fraudulent transaction patterns, transaction behavior, account balance anomalies and predictive modeling techniques to identify potentially fraudulent financial transactions.

## 📌 Project Overview

The purpose of this project is to analyze financial transaction data and uncover insights about:

• 🚨 Fraudulent transactions

• 💸 Transaction amounts

• 🏦 Account balance behavior

• 🔄 Transaction types

• ⏰ Temporal transaction patterns

• 📊 Class imbalance challenges

• 🤖 Machine learning classification models

• 🎯 Fraud detection

This project focuses on:

• Data cleaning

• Memory optimization

• Feature engineering

• Exploratory Data Analysis (EDA)

• Fraud pattern analysis

• Class imbalance handling

• Machine Learning

• Model comparison

• Pipeline construction

• Feature importance analysis

## 📂 Dataset

The dataset contains simulated mobile money transactions generated using PaySim, a financial transaction simulator based on real-world transaction behavior.

Features include:

• Transaction type

• Transaction amount

• Sender account balance before transaction

• Sender account balance after transaction

• Receiver account balance before transaction

• Receiver account balance after transaction

• Fraud indicator

• Flagged fraud indicator

• Transaction timestamp (step)

The dataset is widely used for fraud detection and machine learning classification projects because it contains highly imbalanced transaction data that closely resembles real-world fraud detection challenges.

You can use this [link](https://www.kaggle.com/datasets/mtalaltariq/paysim-data) to download the dataset. 

I didn't provide a ```data``` folder with the dataset as it is quite large (≈482 MB) to upload due to GitHub file size limits.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```📈 SciPy```

• ```🤖 Scikit-learn```

• ```⚡ XGBoost```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

• ```🎨 Aquarel```

• ```🗂️ PyArrow```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed sender and receiver account identifiers

• Renamed balance columns for consistency

• Verified duplicate transactions

• Checked for missing values

• Converted transaction types into categorical variables

• Standardized transaction type formatting

• Verified transaction amounts were non-negative

• Verified account balances were non-negative

• Reordered columns for modeling convenience

• Saved a cleaned dataset for downstream analysis

## ⚙️ Feature Engineering

Several new features were created to improve fraud detection performance.

### 💰 Balance Consistency Features

• Sender Balance Error

• Receiver Balance Error

These features identify transactions where account balances do not reconcile correctly after transfers.

### 📊 Balance Change Features

• Net Change Origin Account

• Net Change Destination Account

These variables measure balance movement before and after transactions.

### 🚨 Transaction Risk Features

• Is Large Transaction

Transactions above the 99th percentile were flagged as potentially high-risk.

### ⏰ Time Features

• Day

• Hour

• Day Of Week

These features capture temporal transaction patterns.

### 📐 Ratio Features

• Amount To Balance Ratio

Measures transaction size relative to the sender's available balance.

These engineered features were added to the final modeling dataset.

## 📊 Exploratory Data Analysis

### 🚨 Fraud Distribution Analysis

• Measured class imbalance

• Evaluated fraud prevalence

• Compared fraudulent and legitimate transaction frequencies

### 💸 Transaction Amount Analysis

• Examined transaction amount distribution

• Measured skewness

• Identified extremely large transactions

### 🏦 Balance Analysis

• Investigated sender balances

• Investigated receiver balances

• Evaluated balance outliers

### 🔄 Transaction Type Analysis

• Compared transaction type frequencies

• Analyzed average transaction amounts by type

### 📈 Fraud Pattern Analysis

• Compared fraud rates across transaction types

• Evaluated fraud rates across days of the week

• Investigated fraud prevalence among large transactions

### 📊 Correlation Analysis

• Examined relationships between existing features and fraud

• Evaluated correlations of engineered features

### 🚨 Outlier Analysis

• Identified transactions above the 99th percentile

• Measured prevalence of extreme transaction amounts

## 🔍 Key Insights

### 🚨 Fraud is extremely rare

The dataset is heavily imbalanced, with approximately 99.9% of transactions being legitimate and only a very small fraction classified as fraudulent.

### 💸 Transaction amounts are highly right-skewed

Most transactions involve relatively modest amounts, while a small number of transactions reach several million currency units.

### 🚨 Large transactions are uncommon

Transactions above the 99th percentile account for only about 1% of all observations.

### 🔄 Fraud is concentrated in specific transaction types

Transfer transactions exhibit substantially higher fraud rates than other transaction categories.

Withdrawals show the second-highest fraud rate, while other transaction types contain very little fraudulent activity.

### 🏦 Balance anomalies are highly informative

Inconsistencies between expected and observed account balances appear to be strong indicators of suspicious activity.

### 📈 Traditional correlations are weak

Most individual features show relatively low linear correlation with fraud, suggesting that complex nonlinear patterns are required for effective detection.

## 🤖 Machine Learning

Four classification models were trained to identify fraudulent transactions.

### 📉 Dummy Classifier

Baseline model that always predicts the majority class.

### 📊 Logistic Regression

Linear classification model with balanced class weighting.

### 🌲 Random Forest Classifier

Ensemble tree-based classifier using multiple decision trees.

### ⚡ XGBoost Classifier

Gradient boosting classifier optimized for imbalanced classification tasks.

### 🔧 Model Pipeline

A reusable preprocessing pipeline was built using:

• ```StandardScaler``` for numerical features

• ```OneHotEncoder(handle_unknown="ignore")``` for categorical features

• ```ColumnTransformer``` for automated preprocessing

The preprocessing pipeline was integrated directly into each machine learning model to ensure consistent transformations during training and inference.

### ⚖️ Class Imbalance Handling

Fraudulent transactions represent only a tiny fraction of observations.

To address this challenge:

• Logistic Regression used ```class_weight="balanced"```

• Random Forest used ```class_weight="balanced"```

• XGBoost used ```scale_pos_weight```

### 📏 Evaluation Metrics

Models were evaluated using:

• Cross-Validation F1 Score

• Accuracy

• Precision

• Recall

• ROC-AUC Score

• F1 Score

## 🏆 Machine Learning Results

### 📉 Dummy Classifier

Served as a baseline by always predicting legitimate transactions.

Key observations:

• Very high accuracy

• Zero fraud detection capability

• Precision = 0

• Recall = 0

• F1 Score = 0

### 📊 Logistic Regression

Logistic Regression achieved:

• Recall ≈ 0.998

• Strong fraud detection capability

Key observations:

• Detected nearly all fraudulent transactions

• Generated many false positives

• Low precision

### 🌲 Random Forest Classifier

Random Forest achieved the strongest overall performance.

Key observations:

• Precision ≈ 1.00

• Recall ≈ 1.00

• F1 Score ≈ 0.999

• Excellent balance between false positives and false negatives

### ⚡ XGBoost Classifier

XGBoost achieved performance comparable to Random Forest.

Key observations:

• Near-perfect fraud detection

• Excellent precision and recall

• Strong ROC-AUC performance

### 🏆 Best Models

The strongest models were:

• Random Forest

• XGBoost

Both substantially outperformed the baseline and Logistic Regression models.

The results suggest that fraudulent transactions in PaySim exhibit highly distinguishable nonlinear patterns that are effectively captured by tree-based ensemble methods.

## 📊 Feature Importance

Feature importance analysis was performed using the Random Forest model.

The most influential predictors included:

• Sender Balance Error

• Net Change Origin Account

• New Balance Origin

• Old Balance Origin

• Amount To Balance Ratio

Several engineered features ranked among the most important predictors, demonstrating that feature engineering contributed significantly to model performance.

Temporal variables such as hour and day of week had comparatively little influence on fraud prediction.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib seaborn scipy scikit-learn xgboost joblib pyarrow aquarel
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

Run the notebooks in the following order:

1. cleaning.ipynb

2. feature_engineering.ipynb

3. EDA.ipynb

4. train.ipynb

5. evaluate.ipynb

## 📚 What I Learned

Through this project I practiced:

• Working with large-scale financial transaction data

• Memory-efficient data processing

• Feature engineering for fraud detection

• Exploratory Data Analysis (EDA)

• Handling severe class imbalance

• Classification model evaluation

• Building preprocessing pipelines

• One-hot encoding categorical variables

• Feature importance interpretation

• Fraud pattern analysis

• Cross-validation

• Ensemble learning methods

• XGBoost classification

• Model persistence using Joblib

• Extracting actionable insights from financial transaction data
