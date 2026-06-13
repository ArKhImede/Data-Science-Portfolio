# 👥 Employee Attrition

Exploratory Data Analysis (EDA) and Machine Learning project focused on understanding employee turnover patterns and predicting employee attrition using workforce, compensation, satisfaction, and career progression data.

## 📌 Project Overview

The purpose of this project is to analyze employee data and uncover insights about:

• 👥 Employee attrition

• 🎂 Workforce demographics

• 💰 Salary and compensation

• ⏰ Overtime and workload

• 😊 Job satisfaction

• ⚖️ Work-life balance

• 📈 Career progression

• 🏢 Department and job role differences

• 🤖 Machine learning classification models

• 🎯 Employee attrition prediction

This project focuses on:

• Data cleaning

• Exploratory Data Analysis (EDA)

• Workforce analytics

• Attrition analysis

• Correlation analysis

• Machine Learning

• Classification modeling

• Model comparison

• Pipeline construction

## 📂 Dataset

The dataset contains employee-level information including:

• Age

• Gender

• Department

• Job Role

• Job Level

• Monthly Income

• Hourly Rate

• Overtime

• Job Satisfaction

• Work-Life Balance

• Performance Rating

• Training Hours

• Project Count

• Years at Company

• Years in Current Role

• Years Since Last Promotion

• Absenteeism

• Distance From Home

• Relationship With Manager

• Employee Attrition

The target variable is:

• Attrition (Yes / No)

The dataset is designed to explore factors that may influence employee turnover and retention.

You can use this [link](https://www.kaggle.com/datasets/ziya07/employee-attrition-prediction-dataset) to download the dataset.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

• ```🔢 NumPy```

• ```📊 Matplotlib```

• ```🤖 Scikit-learn```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

• ```🎨 Aquarel```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Renamed columns for improved readability

• Removed Employee ID as it provides no predictive value

• Inspected missing values

• Checked numerical summary statistics

• Reviewed potential outliers in income and workload-related features

• Standardized column naming conventions

• Saved a cleaned dataset for downstream analysis and modeling

## 📊 Exploratory Data Analysis

### 👥 Attrition Overview

• Examined employee attrition distribution

• Assessed dataset imbalance

### 🎂 Demographics Analysis

Investigated relationships between attrition and:

• Age

• Gender

### 💰 Salary & Compensation Analysis

Explored:

• Monthly Income

• Hourly Rate

• Compensation differences between employees who stayed and left

### ⏰ Overtime & Workload Analysis

Analyzed:

• Overtime participation

• Project Count

• Average Hours Worked Per Week

### 😊 Satisfaction Analysis

Evaluated relationships between attrition and:

• Job Satisfaction

• Work-Life Balance

### 📈 Career Progression Analysis

Explored:

• Years Since Last Promotion

• Years In Current Role

• Career advancement trends

### 🏢 Department & Job Role Analysis

Compared attrition rates across:

• Departments

• Job Roles

### 🔗 Correlation Analysis

Identified numerical variables most associated with attrition.

### 📊 Distribution Analysis

Investigated distributions of:

• Average Hours Worked Per Week

• Years Since Last Promotion

## 🤖 Machine Learning

Three classification models were trained to predict employee attrition.

### 📉 Logistic Regression

Linear classification model with class balancing to address dataset imbalance.

### 🌲 Random Forest Classifier

Ensemble learning model using multiple decision trees.

### 🎯 Support Vector Machine (SVM)

Kernel-based classifier designed to capture nonlinear relationships.

### 🔧 Model Pipeline

A preprocessing pipeline was built using:

• StandardScaler for numerical features

• OneHotEncoder(handle_unknown="ignore") for categorical features

• ColumnTransformer for automated preprocessing

The pipeline was integrated directly into each classification model to ensure consistent feature transformations.

### 📏 Evaluation Metrics

Models were evaluated using:

• Accuracy

• Precision

• Recall

• ROC-AUC

• Confusion Matrix

## 🔍 Key Insights

### 👥 Attrition is relatively uncommon

Approximately 81% of employees remained with the company, resulting in a moderately imbalanced dataset.

### 🎂 Younger employees do not leave more frequently

Employees under 30 years old displayed attrition rates similar to older employees.

### 🚻 Gender has little influence on attrition

Male and female employees exhibited nearly identical turnover rates.

### 💰 Salary alone does not explain attrition

Employees with higher incomes showed attrition rates similar to lower-income employees.

### ⏰ Overtime appears more relevant than compensation

Employees working overtime exhibited higher turnover tendencies compared to those who did not.

### 📋 Project count does not strongly drive attrition

Employees handling larger numbers of projects did not consistently leave more often.

### 😊 Satisfaction metrics show weak relationships

Job Satisfaction and Work-Life Balance exhibited only small differences between employees who stayed and those who left.

### 📈 Promotion delays show limited impact

Long periods without promotion did not produce a clear increase in employee attrition.

### 🏢 Departmental differences exist

Finance employees tended to leave less frequently than employees in HR and IT departments.

### 🔗 Numerical variables show weak correlations

Most numerical features exhibited correlations close to zero with attrition, suggesting limited predictive power.

## 🤖 Machine Learning Results

### 📉 Logistic Regression

Logistic Regression achieved modest performance.

Key observations:

• Slightly better than random guessing

• Identified some attrition cases

• Low precision and recall

### 🎯 Support Vector Machine (SVM)

SVM produced similar results.

Key observations:

• Struggled to identify employees who left

• Low recall

• ROC-AUC close to 0.50

### 🌲 Random Forest Classifier

Random Forest achieved the highest accuracy score.

However:

• Accuracy ≈ 84.5%

• Predicted almost exclusively the majority class

• Failed to correctly identify attrition cases

This demonstrates how accuracy can be misleading when evaluating imbalanced datasets.

### 🏆 Best Overall Model

Although Random Forest achieved the highest accuracy, Logistic Regression provided more meaningful attrition predictions by identifying at least some employees who left.

Overall, all models performed poorly, suggesting that:

• The available features contain limited predictive information

• Employee turnover may be influenced by factors not captured in the dataset

• Additional features or alternative modeling approaches may be required

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```git clone https://github.com/ArKhImede/Data-Science-Portfolio.git```

### 2️⃣ Install dependencies
```pip install pandas numpy matplotlib scikit-learn joblib aquarel```

### 3️⃣ Run Jupyter Notebook
```jupyter notebook```

Run the notebooks in the following order:

1. cleaning.ipynb

2. employee_attrition_analysis.ipynb

3. model_training_and_evaluation.ipynb

## 📚 What I Learned

Through this project I practiced:

• Workforce analytics

• Employee attrition analysis

• Exploratory Data Analysis (EDA)

• Class imbalance assessment

• Binary classification

• Logistic Regression

• Random Forest Classification

• Support Vector Machines

• Building preprocessing pipelines

• One-hot encoding categorical variables

• Feature scaling

• Classification model evaluation

• Precision, Recall, and ROC-AUC interpretation

• Confusion matrix analysis

• Identifying limitations in predictive datasets

• Extracting actionable business insights from HR data
