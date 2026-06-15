# 🌍 OpenAQ Air Quality

Exploratory Data Analysis (EDA), Feature Engineering, Environmental Data Analysis, and Machine Learning project using the OpenAQ air quality dataset. This project explores global pollution measurements, pollutant concentration patterns, geographic effects, temporal trends, and predictive modeling techniques to estimate pollution levels.

## 📌 Project Overview

The purpose of this project is to analyze worldwide air quality measurements and uncover insights about:

• 🌫️ Pollution concentration levels

• 🌍 Geographic pollution patterns

• 🏙️ City and location coverage

• 📅 Seasonal pollution trends

• 🧪 Pollutant type differences

• 📈 Temporal pollution persistence

• 📊 Statistical distribution of pollution measurements

• 🤖 Machine learning regression models

• 🎯 Air quality prediction

This project focuses on:

• Data cleaning

• Missing value handling

• Feature engineering

• Exploratory Data Analysis (EDA)

• Environmental data analysis

• Machine Learning

• Model comparison

• Pipeline construction

## 📂 Dataset

The dataset contains worldwide air quality measurements collected through the OpenAQ platform, including:

• Pollutant concentration values

• Pollutant types

• Geographic coordinates

• Country information

• City information

• Monitoring locations

• Measurement timestamps

• Units of measurement

The OpenAQ dataset aggregates environmental monitoring data from multiple countries and provides a large-scale view of global air quality conditions.

You can use this [link](https://www.kaggle.com/datasets/mexwell/world-air-quality) to download the dataset.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```🔢 NumPy```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```📈 SciPy```

• ```🤖 Scikit-learn```

• ```⚡ XGBoost```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

• ```🎨 Aquarel```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Filled missing categorical values with "Unknown"

• Converted selected string columns to categorical data types

• Converted timestamps to datetime format

• Removed negative pollution values

• Removed unrealistic pollution values exceeding one million units (except for pollutant UM003)

• Preserved missing coordinate values when appropriate

• Optimized data types for memory efficiency

• Saved a cleaned dataset for downstream analysis

## ⚙️ Feature Engineering

Several new features were created to improve interpretability and predictive performance.

### 📈 Temporal Features

• Value Lag 1 Day

• Year

• Month

• Day

### 🔄 Cyclical Date Features

• Month Sin

• Month Cos

### 🌍 Geographic Features

• Latitude

• Longitude

• Has Coordinates

### 🏙️ Location Features

• Has City

### ☣️ Environmental Risk Features

• Pollutant Danger

Pollutants were categorized into risk groups:

• Most Dangerous

• Highly Harmful

• Moderate

• Context-Dependent

• Weather/Environment Factor

## 📊 Exploratory Data Analysis

### 🌫️ Pollution Value Analysis

• Examined pollution concentration distributions

• Measured skewness

• Compared mean and median values

### 📍 Geographic Analysis

• Investigated spatial clustering of pollution measurements

• Evaluated coordinate availability

### 🧪 Pollutant Analysis

• Compared average concentration levels across pollutants

• Identified the highest concentration pollutants

### 🌍 Country Analysis

• Investigated which countries contribute the most measurements

• Compared average pollution levels across countries

### 📅 Seasonal Analysis

• Examined pollution patterns across months

### 📈 Feature vs Target Analysis

• Investigated previous-day pollution values

• Evaluated temporal persistence of pollution measurements

### 🔥 Correlation Analysis

• Identified features most strongly correlated with pollution levels

### 📊 Outlier Analysis

• Measured IQR and percentile ranges

• Investigated extreme pollution observations

## 🤖 Machine Learning

Five regression models were trained to predict pollution concentration levels.

### 📉 Dummy Regressor

Baseline model using the average pollution value.

### 📏 Linear Regression

Traditional linear model used as a simple benchmark.

### 🎯 Support Vector Regression (SVR)

Kernel-based regression model for nonlinear relationships.

### 🌲 Random Forest Regressor

Ensemble model based on multiple decision trees.

### ⚡ XGBoost Regressor

Gradient boosting model designed for high predictive performance.

### 🔧 Model Pipeline

A reusable preprocessing pipeline was built using:

• ```StandardScaler``` for numerical features

• ```OneHotEncoder (handle_unknown="ignore")``` for categorical features

• Median imputation for numerical variables

• Most-frequent imputation for categorical variables

• ```ColumnTransformer``` for automated preprocessing

The preprocessing pipeline was integrated directly into each machine learning model to ensure consistent transformations during training and inference.

### 📏 Evaluation Metrics

Models were evaluated using:

• Cross-Validation R²

• Cross-Validation Standard Deviation

• Test R²

• Mean Absolute Error (MAE)

• Mean Squared Error (MSE)

• Mean Absolute Percentage Error (MAPE)

## 🔍 Key Insights

### 🌫️ Pollution values are highly right-skewed

Most observations contain relatively low pollution levels, while a small number of extreme pollution events create a long right tail.

### 📈 Previous-day pollution is highly predictive

The strongest predictor of pollution concentration is the previous day's recorded value, demonstrating strong temporal persistence.

### 🌍 Pollution monitoring is geographically concentrated

Most measurements originate from the United States, Eastern Asia, and parts of Europe.

### 🧪 Pollutants exhibit substantial concentration differences

UM003 and CO display the highest average concentration values in the dataset.

### 🏙️ Location information matters

Geographic variables account for many of the most important predictive features.

### 📅 Pollution tends to increase late in the year

Average pollution levels are generally higher during October, November, and December.

### 🔥 Extreme pollution events are common

The large difference between upper quartiles and extreme percentiles suggests substantial outliers and heavy-tailed behavior.

### 🌍 Country-level pollution varies considerably

Turkey, India, and China exhibit some of the highest average pollution measurements.

## 🤖 Machine Learning Results

### 📉 Dummy Regressor

The baseline model achieved performance comparable to several more sophisticated models.

This highlights the difficulty of the prediction task.

### 📏 Linear Regression

Linear Regression was the weakest model.

Key observations:

• Negative R² score

• Highest prediction errors

• Failed to capture complex nonlinear relationships

### 🎯 Support Vector Regression (SVR)

SVR performed similarly to the baseline model and showed limited predictive power.

### 🌲 Random Forest Regressor

Random Forest improved prediction performance but showed substantial differences between cross-validation and test results.

This suggests sensitivity to dataset splits.

### ⚡ XGBoost Regressor

XGBoost achieved:

• Lowest MAE

• Lowest MSE

• Best overall predictive performance

However, cross-validation results remained relatively weak, indicating that pollution prediction remains a challenging task.

### 🏆 Best Model

The strongest model was:

• XGBoost Regressor

Feature importance analysis revealed that geographic variables were among the most influential predictors.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```git clone https://github.com/ArKhImede/Data-Science-Portfolio.git```

### 2️⃣ Install dependencies
```pip install pandas numpy matplotlib seaborn scipy scikit-learn xgboost joblib pyarrow aquarel```

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

• Environmental data analysis

• Advanced missing value handling

• Working with large real-world datasets

• Feature engineering for temporal data

• Geographic feature extraction

• Cyclical feature encoding

• Exploratory Data Analysis (EDA)

• Correlation analysis

• Outlier detection

• Building preprocessing pipelines

• Handling mixed numerical and categorical data

• Regression model comparison

• Cross-validation

• Ensemble learning methods

• Feature importance analysis

• Model persistence using Joblib

• Extracting environmental insights from real-world pollution data
