# 🚗 Car Sales Data Analysis

Exploratory Data Analysis (EDA) and Machine Learning project using a car sales dataset. This beginner-to-intermediate project explores car pricing trends, fuel types, mileage patterns, depreciation, and predictive machine learning models using Python.

## 📌 Project Overview

The purpose of this project is to analyze car sales data and uncover insights about:

• 🚘 Car price distributions

• ⛽ Fuel type trends

• 📉 Mileage vs price relationships

• 📈 Car price changes over time

• 🔧 Engine size evolution

• 🚙 Vehicle age distributions

• 🤖 Machine learning models for car price prediction

• 🧠 Price category classification

This project focuses on:

• Data cleaning

• Feature engineering

• Exploratory Data Analysis (EDA)

• Statistical analysis

• Regression models

• Classification models

• Data visualization

• Data visualization

## 📂 Dataset

The dataset contains information about car listings, including:

• Car price

• Fuel type

• Mileage

• Engine size

• Year of manufacture

• Number of owners

• Transmission type

The dataset is used to explore relationships between vehicle characteristics and pricing trends.

To note, I completed the project a few years ago and I don't remember the correct Kaggle link from which I downloaded the dataset. The closest dataset I have found that looks similar to mine is [this](https://www.kaggle.com/datasets/msnbehdani/mock-dataset-of-second-hand-car-sales) one.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• ```🤖 Scikit-learn```

• ```🎨 Aquarel```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed duplicate rows

• Removed missing values

• Standardized column names

• Created a new engineered feature: Car Age

• Converted manufacturing years into age-related metrics

## 📊 Exploratory Data Analysis

### 💰 Price Distribution

• Visualized car price distributions using histograms

• Identified right-skewed pricing patterns

### ⛽ Fuel Type Analysis

• Compared:

  o Petrol
  
  o Diesel
  
  o Hybrid

vehicle counts.

### 📉 Mileage vs Price Relationship

• Explored the relationship between mileage and price

• Colored scatter plots by fuel type

### 📈 Average Price Over Time

• Analyzed how average car prices changed by manufacturing year

• Created animated trend visualizations

### 🚙 Car Longevity Analysis

• Compared mileage statistics between fuel types

• Explored average, minimum, and maximum mileage values

### 🔧 Engine Size Trends

• Compared average engine sizes over time

• Compared engine trends against price increases

### 🕒 Car Age Distribution

• Created histograms showing vehicle age patterns

### 📊 Manufacturing Year vs Price

• Visualized:

  o Mean prices
  
  o Minimum prices
  
  o Maximum prices

across manufacturing years.

## 🤖 Machine Learning

### 📉 Linear Regression

A Linear Regression model was trained to predict car prices using:

• Year of manufacture

The model was evaluated using:

• Mean Squared Error (MSE)

• Mean Absolute Error (MAE)

• Mean Absolute Percentage Error (MAPE)

• R² Score

Residual analysis was also performed to evaluate prediction quality.

### 🌲 Random Forest Classification

A Random Forest Classifier was trained to predict price categories:

• Low-priced cars

• Medium-priced cars

• High-priced cars

The model used features such as:

• Mileage

• Engine size

• Year of manufacture

Hyperparameter tuning was performed using GridSearchCV.

## 🔍 Key Insights

### 💰 Car prices are right-skewed

Most vehicles in the dataset cost less than £50,000, while a smaller number of luxury vehicles exceed £100,000.

### ⛽ Petrol vehicles dominate the dataset

Petrol cars represent the majority of entries compared to diesel and hybrid vehicles.

### 📉 Higher mileage generally means lower prices

Cars with greater mileage tend to depreciate significantly.

### 🚙 Fuel type does not strongly affect average mileage

The dataset suggests similar average mileage values across fuel categories.

### 🔧 Engine sizes stayed relatively stable

While average engine size remained relatively constant over time, average vehicle prices increased substantially.

### 📈 Car prices increased over time

Newer manufacturing years generally correspond to higher average prices.

## 🤖 Machine Learning Results

### 📉 Linear Regression Performance

The regression model achieved:

• R² Score: approximately 0.51

• Mean Absolute Error (MAE): approximately £7,079

The results indicate a moderate relationship between manufacturing year and vehicle price.

### 🌲 Random Forest Classification Performance

The Random Forest Classifier achieved strong classification performance:

• Accuracy: approximately 90%

Key findings include:

• High precision for low-priced cars

• Strong performance detecting expensive vehicles

• Medium-priced vehicles were the hardest category to classify

## ⚠️ Dataset Limitations

One important limitation is that the dataset appears to contain synthetic or artificially generated entries. Some unrealistic feature combinations exist, such as:

• Hybrid vehicles manufactured before hybrid technology became commercially common

Because of this, the dataset is best suited for practicing:

• Data analysis

• Visualization

• Machine learning techniques

rather than drawing real-world automotive market conclusions.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib scikit-learn aquarel
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

## 📚 What I Learned

Through this project I practiced:

• Data cleaning and preprocessing

• Feature engineering

• Exploratory Data Analysis (EDA)

• Statistical visualization

• Regression analysis

• Classification models

• Hyperparameter tuning

• Residual analysis

• Machine learning evaluation metrics
