# 🚲 Bike Sharing Demand Forecasting

Exploratory Data Analysis (EDA), Feature Engineering and Machine Learning project using a Bike Sharing dataset. This project analyzes temporal patterns, weather conditions and historical demand to understand the factors influencing bike rentals and build predictive models for hourly demand estimation.

## 📌 Project Overview

The purpose of this project is to analyze bike sharing demand and uncover insights about:

- 🚲 Hourly rental counts

- 📅 Temporal patterns (hour, day, month, season)

- 🌤️ Weather conditions

- 📈 Historical demand patterns

- 🤖 Machine learning models for demand prediction

This project focuses on:

- Data cleaning

- Data preprocessing

- Feature engineering (cyclical encodings, lag features)

- Exploratory Data Analysis (EDA)

- Data visualization

- Correlation analysis

- Machine Learning (XGBoost, Random Forest, Linear Regression, ARIMA, SARIMA)

- Pipeline construction

- Hyperparameter tuning (GridSearchCV, Optuna)

- Model evaluation

## 📂 Dataset

The dataset contains hourly bike rental counts from a bike sharing system together with temporal and weather information.

The dataset includes features such as:

- Temporal features (datetime, hour, weekday, month, season)

- Weather conditions (temperature, humidity, windspeed, weather situation)

- Holiday indicators

- Rental counts (casual, registered, total)

You can use this [link](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset?select=hour.csv) to download the dataset.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```🎨 Catppuccin```

• ```📈 NumPy```

• ```🌲 Scikit-learn```

• ```🚀 XGBoost```

• ```📉 Statsmodels```

• ```⚡ Optuna```

• ```🔬 SHAP```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

## 🧹 Data Cleaning

Several preprocessing steps were performed to improve data quality before feature engineering.

### 📅 Date Conversion

Converted the `dteday` column from string to datetime format to enable temporal feature extraction.

### 🗑️ Feature Removal

Removed non-informative and leakage features including:

- `instant` (non-informative index)

- `casual` and `registered` (target leakage, as `cnt` = `casual` + `registered`)

### 📊 Sorting

Sorted the DataFrame by datetime and hour to ensure proper temporal ordering for time-series modeling.

## ⚙️ Feature Engineering

Several new features were created to improve predictive performance.

### 📅 Date Features

Extracted from `dteday`:

- `year`

- `day`

### 🔄 Cyclical Encodings

Created sine and cosine transformations to capture cyclical patterns:

- `hour_sin`, `hour_cos` (24-hour cycle)

- `month_sin`, `month_cos` (12-month cycle)

### ⏱️ Lag Features

Engineered historical demand features:

- `cnt_lag_1` (previous hour)

- `cnt_lag_24` (same hour previous day)

- `cnt_lag_168` (same hour previous week)

## 📊 Exploratory Data Analysis

### 📈 Dataset Overview

Explored:

- Dataset dimensions (rows, columns)

- Data types

- Summary statistics

- Duplicate records

- Missing values

### 🚲 Target Variable Analysis

Investigated:

- Rental count distribution

- Skewness and outliers

### 📊 Numerical Feature Analysis

Examined:

- Feature distributions (temp, atemp, hum, windspeed)

- Boxplots

- Skewness

### 📅 Categorical Feature Analysis

Analyzed:

- Seasonal patterns

- Monthly trends

- Hourly patterns

- Holiday effects

### 🔗 Correlation Analysis

Explored relationships between numerical variables and rental counts using a correlation matrix.

### 📉 Feature Relationships

Compared rental counts across:

- Hours of the day

- Months

- Seasons

- Weather conditions

## 🤖 Machine Learning

The objective was to predict hourly bike rental demand.

### 📉 Dummy Regressor

Baseline model using the mean rental count.

### 📈 Linear Regression

Linear benchmark model.

### 🌲 Random Forest Regression

Tree-based ensemble model used for comparison.

### 🚀 XGBoost Regression

Gradient boosting model used as the primary predictive model.

### 📉 ARIMA / SARIMA

Classical time-series models included for comparison (univariate forecasting).

### 🔧 Preprocessing Pipeline

A reusable Scikit-learn pipeline was built using:

- Numerical Features
  - Standard scaling

- Categorical Features
  - One-hot encoding

The preprocessing and model were combined into a single reusable pipeline.

## ⚙️ Hyperparameter Tuning

XGBoost was optimized using two approaches:

### GridSearchCV

The search explored:

- Number of trees (`n_estimators`)

- Learning rate

- Maximum depth

- Subsample ratio

### Optuna

Bayesian optimization explored:

- `n_estimators`

- `learning_rate`

- `max_depth`

- `subsample`

- `colsample_bytree`

### 📏 Evaluation Metrics

Models were evaluated using:

- R² Score

- Mean Absolute Error (MAE)

- Root Mean Squared Error (RMSE)

## 🔍 Key Insights

### 📅 Strong temporal patterns

Bike demand shows clear daily and seasonal patterns, with peaks during morning (8 AM) and evening (5 PM) commuting hours.

### 🌤️ Weather conditions matter

Temperature, humidity and weather situation significantly influence rental counts, with better weather leading to higher demand.

### ⏱️ Historical demand is highly predictive

Lag features (especially `cnt_lag_1`, `cnt_lag_24`, `cnt_lag_168`) are among the most important predictors, capturing recurring demand patterns.

### 🚀 XGBoost outperforms classical models

Gradient boosting substantially outperformed ARIMA/SARIMA by leveraging additional explanatory variables beyond historical demand.

### 📈 Cyclical encodings capture recurring patterns

Sine and cosine transformations of hour and month improved model performance by representing temporal cycles more naturally.

## 🤖 Machine Learning Results

### 📉 Dummy Regressor

Performed poorly, providing a simple baseline for comparison.

### 📈 Linear Regression

Captured linear relationships with an R² of approximately 0.86, indicating strong linear components in the data.

### 🌲 Random Forest

Produced strong predictive performance with good generalization.

### 🚀 XGBoost

Achieved the best overall performance:

- Test R²: 0.90

- MAE: ~29 bikes

- RMSE: ~46 bikes

On average, predictions are off by about 29 bikes per hour.

### 📉 ARIMA / SARIMA

Substantially underperformed XGBoost due to reliance solely on historical demand without weather or calendar features.

### ⚙️ Hyperparameter Tuning

Both GridSearchCV and Optuna improved the XGBoost model slightly, with Optuna showing more efficient exploration of the hyperparameter space.

## 📈 Model Evaluation

The final model was evaluated using several diagnostic techniques.

Performed:

- Actual vs Predicted analysis

- Residual distribution analysis

- Residual scatter plots

- Feature importance analysis

- SHAP values for interpretability

- Error analysis by season and month

- Comparison with classical forecasting models

The evaluation showed good generalization with no systematic over- or under-prediction, though prediction uncertainty increases for higher demand periods.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas numpy matplotlib seaborn scikit-learn xgboost statsmodels optuna shap joblib pyarrow catppuccin
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

Run the notebooks in the following order:

- 01_EDA.ipynb

- 02_Preprocessing.ipynb

- 03_Feature_Engineering.ipynb

- 04_Modeling.ipynb

- 05_Hyperparameter_Tuning.ipynb

- 06_Classical_Forecasting.ipynb

- 07_Optuna_Optimization.ipynb

- 08_Model_Evaluation.ipynb

## 📚 What I Learned

Through this project I practiced:

- Working with real-world time-series datasets

- Building reusable preprocessing functions

- Creating feature engineering pipelines

- Handling datetime features and cyclical encodings

- Engineering lag features for time-series modeling

- Exploratory Data Analysis (EDA)

- Correlation analysis

- Building Scikit-learn preprocessing pipelines

- Comparing multiple regression models (XGBoost, Random Forest, Linear Regression)

- Implementing classical forecasting models (ARIMA, SARIMA)

- Hyperparameter tuning using GridSearchCV and Optuna

- Evaluating regression models with diagnostic plots

- Interpreting feature importance and SHAP values

- Saving complete machine learning pipelines using Joblib

- Building a reproducible end-to-end machine learning workflow

- Time-series aware train/test splitting
