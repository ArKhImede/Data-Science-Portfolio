# 🏪 Rossmann Store Sales Forecasting

Exploratory Data Analysis (EDA), Feature Engineering and Machine Learning project using the Rossmann Store Sales dataset. This project analyzes store characteristics, promotions, seasonality and competition effects to understand sales behavior and build predictive models for daily sales forecasting.

## 📌 Project Overview

The purpose of this project is to analyze retail sales data and uncover insights about:

• 💰 Daily store sales

• 👥 Customer traffic patterns

• 🎯 Promotion effectiveness

• 🏫 School holiday effects

• 🏬 Store characteristics

• 🏷️ Assortment strategies

• 🏪 Competition impact

• 📅 Seasonal and temporal trends

• 🤖 Machine learning models for sales forecasting

This project focuses on:

• Data cleaning

• Data integration

• Feature engineering

• Exploratory Data Analysis (EDA)

• Data visualization

• Statistical analysis

• Machine Learning

• Pipeline construction

• Hyperparameter tuning

• Business insight extraction

## 📂 Dataset

The dataset comes from the Rossmann Store Sales forecasting competition and contains historical daily sales data for Rossmann stores together with store metadata.

The project combines the available datasets into analytical tables suitable for both business analysis and machine learning.

The main datasets include:

• Store information

• Historical daily sales records

• Promotion information

• Competition information

You can use this [link](https://www.kaggle.com/datasets/shahpranshu27/rossman-store-sales) to download the dataset.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```📈 SciPy```

• ```📉 Statsmodels```

• ```🌲 Scikit-learn```

• ```🚀 XGBoost```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

• ```🎨 Catppuccin```

## 🧹 Data Cleaning

Several preprocessing steps were performed to improve data quality and reduce memory usage.

### 🏷️ Data Type Optimization

Optimized numerical columns using smaller integer types to reduce memory consumption.

Categorical conversion was applied to:

• Store Type

• Assortment

• State Holiday

• Promotion Intervals

### 🧩 Missing Value Handling

Missing values were handled using domain-specific rules:

• Competition distance was imputed using the median value.

• Competition opening dates were filled with zeros when competition did not exist.

• Promotion start dates were filled with zeros for stores not participating in Promo2.

• Missing promotion intervals were replaced with "None".

### 🔗 Dataset Integration

Merged:

• Store information

• Daily sales data

into a single analytical dataset.

### ✅ Data Validation

Performed checks for:

• Missing values

• Duplicate records

• Negative values in numerical features

• Data consistency after merging

## ⚙️ Feature Engineering

Several additional features were created to improve model performance.

### 📅 Date Features

Extracted:

• Year

• Month

• Day

• Week of Year

• Quarter

• Weekend Indicator

### 🌤️ Seasonal Features

Created:

• Season

using calendar dates.

### 🏪 Competition Features

Created:

• Competition Exists

• Competition Age in Months

to measure both presence and maturity of competitors.

### 🎯 Promotion Features

Created:

• Was Promo2 Active

which determines whether a store's continuous promotion program was active on a given date.

## 📊 Exploratory Data Analysis

### 💰 Sales Analysis

Investigated:

• Sales distribution

• Skewness

• Extreme values

### 👥 Customer Analysis

Explored:

• Customer count distributions

• Outlier detection using Z-scores

### 🎯 Promotion Analysis

Analyzed:

• Promotion participation rates

• Sales differences during promotions

• Continuous promotion strategies

### 🏪 Competition Analysis

Investigated:

• Competition distance

• Competition age

• Customer behavior under competition pressure

### 🏷️ Store Characteristics

Compared:

• Store types

• Assortment levels

• Customer counts

• Sales performance

### 📅 Temporal Analysis

Examined:

• Monthly sales trends

• Seasonal behavior

• Weekly sales cycles

### 📈 Correlation Analysis

Explored relationships between:

• Customers

• Promotions

• Competition variables

• Sales

### 📊 Statistical Analysis

Performed:

• Mann-Whitney U tests

• ANOVA tests

• Tukey HSD comparisons

• Variance Inflation Factor (VIF) analysis

• Time series decomposition

## 🤖 Machine Learning

The objective was to predict daily store sales.

### 📉 Dummy Regressor

Baseline model using median sales predictions.

### 📈 Multiple Linear Regression

Linear model used to establish a strong interpretable benchmark.

### 🌲 Random Forest Regression

Tree-based ensemble model designed to capture nonlinear relationships and interactions.

### 🚀 XGBoost Regression

Gradient boosting model optimized for predictive performance.

### 🔧 Preprocessing Pipeline

A reusable preprocessing pipeline was built using:

Numerical Features

• Standard scaling

Categorical Features

• One-hot encoding

### ⏱️ Time Series Cross Validation

Traditional random cross-validation was avoided to prevent data leakage.

Instead, the project uses:

• TimeSeriesSplit cross-validation

to preserve temporal ordering.

### ⚙️ Hyperparameter Tuning

Random Forest hyperparameters were optimized using GridSearchCV.

The search explored:

• Number of trees

• Maximum depth

• Minimum samples per split

• Minimum samples per leaf

### 📏 Evaluation Metrics

Models were evaluated using:

• R² Score

• Mean Absolute Error (MAE)

• Mean Squared Error (MSE)

• Mean Absolute Percentage Error (MAPE)

## 🔍 Key Insights

### 👥 Customer counts strongly drive sales

Customers exhibit the strongest relationship with sales, with a correlation of approximately 0.89.

### 🎯 Promotions significantly increase sales

Statistical testing showed that promotional periods produce significantly different sales distributions compared to non-promotional periods.

### 🎄 December is the strongest sales month

Sales peak during December regardless of continuous promotion participation.

### 🏷️ Extra assortment stores generate higher sales

Stores offering the largest assortment category tend to attract more customers and produce higher revenue.

### 📅 Sales follow a strong weekly pattern

Time series decomposition revealed highly regular weekly seasonality driven largely by store closures.

### 🏪 Competition effects are limited

Competition proximity appears to have relatively little impact on customer counts.

### 🏫 School holidays influence sales

Sales distributions differ significantly during school holiday periods according to the Mann-Whitney U test.

## 🤖 Machine Learning Results

### 📉 Dummy Regressor

As expected, the baseline model performed poorly and produced an R² score close to zero.

### 📈 Linear Regression

Linear Regression achieved strong performance with an R² score of approximately 0.88, indicating that linear relationships explain much of the variation in sales.

### 🌲 Random Forest

Random Forest achieved a test R² score close to 0.98 and produced the lowest prediction errors among all models.

### 🚀 XGBoost

XGBoost achieved performance comparable to Random Forest, also reaching an R² score close to 0.98.

### ⚙️ Hyperparameter Tuning Results

GridSearchCV identified the best Random Forest configuration as:

• 300 trees

• Unlimited tree depth

• Minimum samples split of 2

• Minimum samples leaf of 1

The tuned model achieved a cross-validation R² score of approximately 0.979.

### 🏆 Best Model

Random Forest provided the best balance between predictive accuracy and stability, outperforming both the linear baseline and the untuned ensemble models.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```git clone https://github.com/ArKhImede/Data-Science-Portfolio.git```

### 2️⃣ Install dependencies
```pip install pandas matplotlib seaborn scipy statsmodels scikit-learn xgboost joblib pyarrow catppuccin```

### 3️⃣ Run Jupyter Notebook
```jupyter notebook```

Run the notebooks in the following order:

1. cleaning.ipynb

2. feature_engineering.ipynb

3. EDA.ipynb

4. train.ipynb

5. tune_best_model.ipynb

6. evaluate.ipynb

## 📚 What I Learned

Through this project I practiced:

• Working with large retail datasets

• Memory optimization techniques

• Building reusable preprocessing pipelines

• Time-aware train/validation splitting

• Feature engineering for time series data

• Statistical hypothesis testing

• Time series decomposition

• Cross-validation for temporal data

• Hyperparameter tuning with GridSearchCV

• Ensemble learning methods

• Model comparison and evaluation

• Saving machine learning pipelines using Joblib

• Extracting business insights from retail sales data

• Building reproducible machine learning workflows
