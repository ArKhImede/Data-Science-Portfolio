# 📞 Telco Customer Churn Prediction

Exploratory Data Analysis (EDA), Feature Engineering, Statistical Analysis, and Machine Learning project using the Telco Customer Churn dataset. This project investigates customer behavior, service usage patterns, churn drivers, and predictive modeling techniques to identify customers at risk of leaving a telecommunications provider.

## 📌 Project Overview

The purpose of this project is to analyze customer subscription data and uncover insights about:

• 📉 Customer churn

• 💰 Monthly and total charges

• 📅 Customer tenure

• 📞 Service adoption

• 🛡️ Support and security services

• 📄 Contract types

• 📊 Statistical differences across customer groups

• 🤖 Machine learning classification models

• 🎯 Churn prediction

This project focuses on:

• Data cleaning

• Memory optimization

• Feature engineering

• Exploratory Data Analysis (EDA)

• Statistical hypothesis testing

• Class imbalance handling

• Machine Learning

• Model comparison

• Pipeline construction

• Feature importance analysis

## 📂 Dataset

The dataset contains information about telecommunications customers, including demographics, subscription details, billing information, and churn status.

Features include:

• Customer demographics

• Tenure

• Monthly charges

• Total charges

• Contract type

• Payment method

• Internet service

• Phone service

• Streaming services

• Security and support services

• Churn status

The dataset is widely used for customer retention and churn prediction projects because it closely resembles real-world subscription-based business problems.

You can use this [link](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) to download the dataset.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```📈 SciPy```

• ```📊 Statsmodels```

• ```🤖 Scikit-learn```

• ```⚡ XGBoost```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

• ```🎨 Aquarel```

• ```🗂️ PyArrow```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed customer identifiers

• Corrected column naming inconsistencies

• Converted TotalCharges to a numerical variable

• Handled invalid TotalCharges values

• Filled missing TotalCharges values with 0

• Converted categorical variables into category data types

• Optimized numerical data types for memory efficiency

• Verified duplicate records

• Verified missing values

• Saved a cleaned dataset for downstream analysis

## ⚙️ Feature Engineering

Several new features were created to improve interpretability and predictive performance.

### 📞 Service Usage Features

• Number of Services

Counts the total services subscribed to by a customer.

### 📅 Customer Lifecycle Features

• Long Time Customer

• New Customer

• Tenure Group

These features capture customer maturity and retention behavior.

### 💰 Spending Features

• High Spender

Identifies customers whose total spending falls above the 90th percentile.

### 💳 Payment Features

• Auto Payment

Flags customers using automatic payment methods.

### 🛡️ Support Features

• Has Support Services

Identifies customers with security, protection, or technical support services.

These engineered features were added to the final modeling dataset.

## 📊 Exploratory Data Analysis

### 📉 Churn Analysis

• Examined churn distribution

• Evaluated class imbalance

### 💰 Monthly Charges Analysis

• Investigated distribution shape

• Measured skewness

• Compared mean and median values

### 📅 Customer Tenure Analysis

• Investigated long-term customer behavior

• Examined customer retention patterns

### 👥 Customer Segment Analysis

• Compared tenure across genders

• Investigated spending differences between customer groups

### 📞 Service Analysis

• Evaluated support and security services

• Compared churn rates across service categories

### 📄 Contract Analysis

• Compared churn rates across contract types

• Investigated retention differences between contracts

### 📊 Correlation Analysis

• Examined relationships between numerical features

• Evaluated correlations with churn

### 📈 ANOVA & Tukey HSD

• Tested whether monthly charges differed across payment methods

• Identified which payment method groups significantly differed

## 🔍 Key Insights

### 📉 Churn is moderately imbalanced

Approximately 73.5% of customers remained with the company, while 26.5% churned.

### 💰 Monthly charges exhibit a bimodal distribution

Customers appear to cluster into lower-cost and higher-cost subscription groups, suggesting distinct customer segments.

### 👥 Gender has little impact on customer retention

Tenure distributions are similar across male and female customers.

### 💸 Customers who churn pay more

Customers who leave the service generally have higher monthly charges than customers who remain.

### 👴 Senior citizens churn more frequently

Senior customers exhibit noticeably higher churn rates compared to non-senior customers.

### 🛡️ Support services improve retention

Customers using technical support, device protection, and online security services churn substantially less often.

### 📄 Contract type is one of the strongest churn drivers

Two-year contracts exhibit extremely low churn rates compared to month-to-month customers.

### 📅 Customer tenure strongly affects churn

Newer customers churn considerably more often than long-term subscribers.

### 📊 Payment methods differ significantly

ANOVA results showed statistically significant differences in monthly charges across payment methods.

Tukey HSD analysis revealed that nearly all payment method pairs differed significantly except bank transfer and credit card automatic payments.

## 🤖 Machine Learning

Four classification models were trained to predict customer churn.

### 📉 Dummy Classifier

Baseline model that predicts the majority class.

### 📊 Logistic Regression

Linear classification model with balanced class weighting.

### 🌲 Random Forest Classifier

Ensemble tree-based classifier using multiple decision trees.

### ⚡ XGBoost Classifier

Gradient boosting classifier designed for strong predictive performance.

### 🔧 Model Pipeline

A reusable preprocessing pipeline was built using:

• ```StandardScaler``` for numerical features

• ```OneHotEncoder(handle_unknown="ignore")``` for categorical features

• ```ColumnTransformer``` for automated preprocessing

The preprocessing pipeline was integrated directly into each machine learning model to ensure consistent transformations during training and inference.

### ⚖️ Class Imbalance Handling

To address class imbalance:

• Logistic Regression used ```class_weight="balanced"```

• Random Forest used ```class_weight="balanced"```

• XGBoost used ```scale_pos_weight```

### 📏 Evaluation Metrics

Models were evaluated using:

• Cross-Validation F1 Score

• Test Accuracy

• Precision

• Recall

• ROC-AUC Score

• F1 Score

## 🤖 Machine Learning Results

### 📉 Dummy Classifier

Served as a baseline model by always predicting the majority class.

Key observations:

• Accuracy ≈ 73%

• Failed to identify churned customers

• Precision = 0

• Recall = 0

• F1 Score = 0

### 📊 Logistic Regression

Logistic Regression achieved the strongest overall balance between precision and recall.

Key observations:

• Precision ≈ 51%

• Recall ≈ 80%

• F1 Score ≈ 62%

• Best overall F1 Score

### 🌲 Random Forest Classifier

Random Forest achieved:

• Highest Accuracy ≈ 78%

• Highest Precision ≈ 61%

• Strong ROC-AUC performance

### ⚡ XGBoost Classifier

XGBoost achieved performance comparable to Random Forest.

Key observations:

• Strong classification performance

• High ROC-AUC score

• Competitive precision and recall

## 📊 Feature Importance

Feature importance analysis was performed using the XGBoost model.

The most influential predictors included:

• Month-to-Month Contract

• Fiber Optic Internet Service

• Online Security

• Tech Support

• Two-Year Contract

• One-Year Contract

Contract-related variables dominated feature importance rankings, confirming insights observed during exploratory analysis.

Support and security services also ranked among the strongest predictors of customer retention.

### 🏆 Best Model

Although Random Forest and XGBoost achieved slightly higher accuracy and precision, Logistic Regression achieved the highest F1 Score and the strongest balance between identifying churners and minimizing false positives.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```git clone https://github.com/ArKhImede/Data-Science-Portfolio.git```

### 2️⃣ Install dependencies
```pip install pandas matplotlib seaborn scipy statsmodels scikit-learn xgboost joblib pyarrow aquarel```

### 3️⃣ Run Jupyter Notebook
```jupyter notebook```

Run the notebooks in the following order:

1. cleaning.ipynb

2. feature_engineering.ipynb

3. EDA.ipynb

4. train.ipynb

5. evaluate.ipynb

## 📚 What I Learned

Through this project I practiced:

• Customer churn analysis

• Memory-efficient data processing

• Feature engineering for subscription businesses

• Exploratory Data Analysis (EDA)

• Statistical hypothesis testing using ANOVA

• Tukey HSD post-hoc analysis

• Handling imbalanced classification problems

• Building preprocessing pipelines

• One-hot encoding categorical variables

• Cross-validation

• Classification model evaluation

• Ensemble learning methods

• XGBoost classification

• Feature importance interpretation

• Customer retention analytics

• Extracting actionable business insights from customer subscription data
