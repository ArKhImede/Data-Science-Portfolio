# 🚀 Spaceship Titanic

Exploratory Data Analysis (EDA), Feature Engineering, and Machine Learning project using the Spaceship Titanic dataset. This project explores passenger characteristics, spending behavior, cabin information, and transportation outcomes to predict whether a passenger was transported to an alternate dimension.

## 📌 Project Overview

The purpose of this project is to analyze passenger data and uncover insights about:

• 👨‍🚀 Passenger demographics

• 🛌 CryoSleep behavior

• 💳 Spending patterns

• 🏠 Cabin location

• 👥 Group travel dynamics

• 🌍 Home planet and destination effects

• 📊 Transportation probabilities

• 🤖 Machine learning classification models

• 🎯 Passenger transportation prediction

This project focuses on:

• Data cleaning

• Missing value handling

• Feature engineering

• Exploratory Data Analysis (EDA)

• Machine Learning

• Model comparison

• Pipeline construction

## 📂 Dataset

The dataset contains information about passengers aboard the fictional Spaceship Titanic, including:

• Passenger ID

• Home Planet

• Destination

• Age

• VIP status

• CryoSleep status

• Cabin information

• Spending across onboard services

• Passenger name

• Transportation outcome

The goal is to predict whether a passenger was transported during the anomaly event.

You can use this [link](https://www.kaggle.com/datasets/jyothishri/spaceship-titanic?select=Spaceship_train.csv) to download the dataset.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```🔢 NumPy```

• ```📊 Matplotlib```

• ```🤖 Scikit-learn```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

• ```🎨 Aquarel```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Filled missing CryoSleep values with False

• Extracted passenger surnames from the Name column

• Removed the original Name column

• Filled missing Cabin values with "Unknown"

• Filled missing numerical values using median imputation

• Filled missing categorical values using mode imputation

• Reordered columns to place the target variable at the end

• Saved a cleaned dataset for downstream analysis

## ⚙️ Feature Engineering

Several new features were created to improve interpretability and predictive performance.

### 🚪 Cabin Features

• Deck

• Cabin Number

• Side of Ship

### 👥 Passenger Group Features

• Group Number

• Passengers Within Group

• Group Size

• Is Alone

### 💳 Spending Features

• Total Spend

• Luxury Spending

• Basic Spending

• Spending Per Person

• No Spending

### 📈 Behavioral Features

• CryoSleep status

• VIP status

• Spending behavior indicators

These engineered features were added to the final modeling dataset.

## 📊 Exploratory Data Analysis

### 🎯 Transportation Analysis

• Examined class balance

• Measured transportation percentages

### ❓ Missing Values Review

• Evaluated remaining "Unknown" values

• Verified cleaning effectiveness

### 👶 Age Analysis

• Investigated age distribution

• Measured skewness

• Compared transportation rates across age groups

### 💳 Spending Behavior Analysis

• Examined spending distributions

• Identified spending outliers

• Compared spending patterns with transportation outcomes

### 🌍 Passenger Characteristics

Compared transportation rates across:

• Home planets

• Destinations

• VIP status

• CryoSleep status

### 👥 Group Analysis

• Investigated transportation rates by group size

• Evaluated the effect of traveling alone

### 🚪 Cabin Analysis

• Compared transportation rates across decks

• Examined ship-side effects

### 📈 Correlation Analysis

• Identified numerical features most associated with transportation

## 🤖 Machine Learning

Three classification models were trained to predict transportation outcomes.

### 📉 Logistic Regression

Linear classification model used as a strong baseline.

### 🌲 Random Forest Classifier

Ensemble tree-based classifier using multiple decision trees.

### 🎯 Support Vector Machine (SVM)

Kernel-based classifier using a radial basis function (RBF) kernel.

### 🔧 Model Pipeline

A reusable preprocessing pipeline was built using:

• ```StandardScaler``` for numerical features

• ```OneHotEncoder(handle_unknown="ignore")``` for categorical features

• ```ColumnTransformer``` for automated preprocessing

The preprocessing pipeline was integrated directly into each machine learning model to ensure consistent transformations during training and inference.

### 📏 Evaluation Metrics

Models were evaluated using:

• Accuracy

• Precision

• Recall

• ROC AUC

## 🔍 Key Insights

### 🛌 CryoSleep strongly influences transportation

Passengers in CryoSleep were transported at much higher rates than awake passengers.

### 💳 Spending behavior is highly predictive

Passengers with little or no spending activity were substantially more likely to be transported.

### 👶 Children are transported more frequently

Approximately two-thirds of children were transported, a noticeably higher proportion than other age groups.

### 🌍 Passenger origin matters

Transportation rates vary significantly depending on passengers' home planets and destinations.

### 🚪 Deck location impacts outcomes

Some decks exhibit much higher transportation rates than others, suggesting location-based effects.

### 📈 No single numerical feature dominates

While several engineered features provide useful information, transportation appears to be influenced by multiple interacting factors.

## 🤖 Machine Learning Results

### 📉 Logistic Regression

Logistic Regression achieved strong performance despite its simplicity, demonstrating that many transportation patterns are approximately linear.

### 🎯 Support Vector Machine (SVM)

SVM achieved competitive performance and effectively captured nonlinear relationships within the dataset.

### 🌲 Random Forest Classifier

Random Forest achieved the strongest overall performance:

• Accuracy ≈ 80%

• Precision ≈ 81.7%

• ROC AUC ≈ 0.897

The model successfully captured nonlinear feature interactions and complex passenger behavior patterns.

### 🏆 Best Model

The best-performing model was:

• Random Forest Classifier

Its superior ROC AUC and classification performance suggest that transportation outcomes depend heavily on nonlinear relationships between passenger characteristics, spending behavior, and cabin information.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```git clone https://github.com/ArKhImede/Data-Science-Portfolio.git```

### 2️⃣ Install dependencies
```pip install pandas numpy matplotlib scikit-learn joblib aquarel```

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

• Missing value handling

• Feature engineering

• Exploratory Data Analysis (EDA)

• Passenger behavior analysis

• Working with categorical and numerical features

• Building preprocessing pipelines

• One-hot encoding

• Classification model development

• Model comparison and benchmarking

• ROC AUC evaluation

• Ensemble learning methods

• Model persistence using Joblib

• Extracting insights from complex tabular datasets
