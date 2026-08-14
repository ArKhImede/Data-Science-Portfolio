# 🛒 Instacart Market Basket Analysis

Exploratory Data Analysis (EDA), Feature Engineering, Data Engineering, and Machine Learning project using the Instacart Online Grocery Shopping Dataset. This project explores customer purchasing behavior, reorder patterns, basket composition, product popularity, and predictive modeling techniques to identify whether a customer will reorder a product.

## 📌 Project Overview

The purpose of this project is to analyze large-scale grocery shopping behavior and uncover insights about:

• 🛒 Customer purchasing habits

• 🔁 Product reordering behavior

• 👥 User shopping patterns

• 🥬 Product popularity

• 🏪 Department and aisle preferences

• ⏰ Ordering time trends

• 📦 Basket size behavior

• 🤖 Machine learning classification models

• 🎯 Reorder prediction

This project focuses on:

• Data cleaning

• Memory optimization

• Dataset integration

• Feature engineering

• Exploratory Data Analysis (EDA)

• Customer behavior analysis

• Machine Learning

• Model comparison

• Pipeline construction

## 📂 Dataset

The dataset contains anonymized grocery shopping transactions from Instacart, including:

• Customer orders

• Product information

• Department information

• Aisle information

• Reorder indicators

• Order timing information

• Basket composition

• Customer purchase history

The project combines multiple relational datasets into a unified analytical dataset suitable for EDA and machine learning.

The dataset includes millions of purchase events and represents real-world e-commerce purchasing behavior.

You can use this [link](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis) to download the dataset.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```🔢 NumPy```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```🤖 Scikit-learn```

• ```⚡ XGBoost```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

• ```🎨 Aquarel```

• ```🗄️ PyArrow```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Optimized data types to reduce memory consumption

• Loaded and validated all relational datasets

• Merged orders, products, aisles, and departments tables

• Verified merge integrity using assertions

• Converted categorical columns to category data types

• Created analytical datasets for users and products

• Generated average basket size statistics

• Saved processed datasets using Parquet format for improved performance

## ⚙️ Feature Engineering

Several new features were created to improve analysis and predictive modeling:

### ⏰ Time-Based Features

• Part Of Day Purchase

- Morning

- Afternoon

- Evening

- Night

### 🏷️ Product Features

• Product Name Length

### ❓ Missing Value Indicators

• Days Since Prior Order Missing

These engineered features were added to the final modeling dataset.

## 📊 Exploratory Data Analysis

### 🧺 Basket Size Analysis

• Investigated average basket size distribution

• Measured skewness

• Evaluated purchasing variability across users

### 🥬 Product Popularity Analysis

• Identified most frequently ordered products

• Compared product ordering frequency

### 👥 Customer Behavior Analysis

• Examined user ordering distributions

• Analyzed reorder tendencies across customers

### 🔁 Reorder Analysis

• Investigated target variable balance

• Measured overall reorder rates

### ⏰ Temporal Analysis

• Explored ordering behavior by day of week

• Investigated ordering behavior by hour of day

• Examined preferred parts of the day

### 🏪 Category Analysis

Compared customer preferences across:

• Aisles

• Departments

• Product categories

### 📈 Correlation Analysis

• Evaluated relationships between numerical features

• Identified variables associated with reordering behavior

### 📊 Group Analysis

• Compared ordering patterns across different times of day

• Investigated preferred ordering hours

## 🤖 Machine Learning

Three classification models were trained to predict whether a product would be reordered.

### 📉 Logistic Regression

Linear classification model used as a strong baseline.

### 🌲 Random Forest Classifier

Ensemble tree-based model capable of capturing nonlinear relationships.

### ⚡ XGBoost Classifier

Gradient boosting model designed for high predictive performance on structured tabular data.

### 🔧 Model Pipeline

A reusable preprocessing pipeline was built using:

• Median imputation for numerical features

• Most frequent imputation for categorical features

• ```StandardScaler``` for numerical features

• ```OneHotEncoder(handle_unknown="ignore")``` for categorical features

• ```ColumnTransformer``` for automated preprocessing

The preprocessing pipeline was integrated directly into each machine learning model to ensure consistent transformations during training and inference.

### 🎯 Data Leakage Prevention

To create realistic evaluation conditions:

• Training and test sets were split by user rather than individual rows

• Users appearing in the training set never appeared in the test set

• Leakage-related identifiers were removed before model training

This approach better simulates real-world prediction scenarios.

### 📏 Evaluation Metrics

Models were evaluated using:

• Accuracy

• Precision

• Recall

• ROC AUC

## 🔍 Key Insights

### 🧺 Basket sizes are right-skewed

Most users purchase a moderate number of products per order, while a smaller number of customers create unusually large baskets.

### 🥬 Fresh produce dominates purchases

The most ordered products include:

• Bananas

• Organic Strawberries

• Organic Baby Spinach

Produce-related categories consistently appear among the most popular purchases.

### 👥 Customer purchasing behavior is highly variable

Some users place only a few orders while others become highly active repeat customers.

### 🔁 Reordering is extremely common

Approximately 59% of purchase events correspond to reordered products, indicating strong customer loyalty and habitual purchasing behavior.

### 📅 Customers prefer ordering at the beginning of the week

Order volumes are highest on:

• Sunday

• Monday

Ordering activity decreases throughout most of the week before increasing again later.

### ⏰ Late morning is the most popular ordering period

Customers tend to place orders most frequently during:

• 10 AM

• 11 AM

Ordering activity gradually decreases later in the day.

### 🏪 Produce is the dominant department

Fresh fruits and vegetables represent the most popular aisles and departments across the dataset.

### 📈 Numerical correlations are generally weak

Most numerical variables exhibit relatively small correlations with reordering behavior.

The strongest relationship observed was:

• Order Number (~0.31)

indicating that experienced customers are somewhat more likely to reorder products.

## 🤖 Machine Learning Results

### 📉 Logistic Regression

Logistic Regression achieved:

• Accuracy ≈ 72%

• Precision ≈ 78%

• Recall ≈ 64%

• ROC AUC ≈ 0.79

The model produced the highest precision score, meaning reorder predictions were often correct when made.

### 🌲 Random Forest Classifier

Random Forest achieved:

• Accuracy ≈ 73%

• Precision ≈ 72%

• Recall ≈ 80%

• ROC AUC ≈ 0.79

The model improved recall substantially compared to Logistic Regression.

### ⚡ XGBoost Classifier

XGBoost achieved:

• Accuracy ≈ 74%

• Precision ≈ 73%

• Recall ≈ 86%

• ROC AUC ≈ 0.80

XGBoost provided the strongest overall balance between identifying reorder events and minimizing classification errors.

### 🏆 Best Model

The strongest model was:

• XGBoost Classifier

Key advantages:

• Highest accuracy

• Highest recall

• Highest ROC AUC score

• Best overall ability to identify reorder events

The results suggest that customer reordering behavior contains meaningful patterns that gradient boosting methods can effectively capture.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib pyarrow aquarel
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

• Working with large-scale relational datasets

• Memory optimization techniques in Pandas

• Dataset integration and merging

• Feature engineering

• Exploratory Data Analysis (EDA)

• Customer behavior analytics

• Handling categorical data

• Building preprocessing pipelines

• Preventing data leakage

• Machine learning classification

• Model comparison and benchmarking

• Working with imbalanced targets

• Evaluating classification models

• Saving models using Joblib

• Using Parquet for efficient data storage

• Extracting business insights from e-commerce purchasing behavior
