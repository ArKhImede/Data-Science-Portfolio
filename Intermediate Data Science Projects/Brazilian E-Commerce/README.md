# 🛒 Olist E-Commerce 

Exploratory Data Analysis (EDA), Feature Engineering, and Machine Learning project using the Brazilian Olist E-Commerce dataset. This project explores customer purchasing behavior, product characteristics, delivery performance, payment methods, and review score prediction using Python.

## 📌 Project Overview

The purpose of this project is to analyze e-commerce transactions and uncover insights about:

• ⭐ Customer review scores

• 📦 Order and delivery performance

• 💳 Payment methods

• 🏙️ Customer purchasing behavior

• 🛍️ Product categories

• 🚚 Freight and shipping costs

• 📊 Customer satisfaction drivers

• 🤖 Machine learning models for review score prediction

This project focuses on:

• Data cleaning

• Data integration

• Feature engineering

• Exploratory Data Analysis (EDA)

• Data visualization

• Machine Learning

• Pipeline construction

• Business insight extraction

## 📂 Dataset

The dataset comes from the Brazilian Olist marketplace and consists of multiple relational tables containing information about:

• Customers

• Orders

• Payments

• Reviews

• Products

• Order items

The project combines these datasets into analytical tables suitable for business analysis and machine learning.

You can use this [link](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_customers_dataset.csv) to download the dataset.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

• ```🔢 NumPy```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```🤖 Scikit-learn```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

## 🧹 Data Cleaning

The original dataset was distributed across multiple tables.

Several preprocessing steps were performed:

### 📅 Date Handling

Converted timestamp columns into datetime format for:

• Orders

• Reviews

• Shipping information

### 🏙️ Text Standardization

• Standardized city names

• Cleaned product category names

• Cleaned payment type labels

### 🔗 Dataset Integration

Merged:

• Customers

• Orders

• Reviews

• Payments

• Order Items

into a unified analytical dataset.

### 📦 Order-Level Aggregations

Created order-level metrics including:

• Total order price

• Total freight cost

• Number of items purchased

• Total payment value

• Maximum installment count

### 🧹 Duplicate Handling

• Removed duplicate reviews

• Aggregated duplicated order entries

## ⚙️ Feature Engineering

Additional features were created to improve analysis:

### 💰 Spending Features

• Total Spend

• Freight Per Price Ratio

### 🏷️ Product Pricing Features

Products were categorized into:

• Low Price

• Medium Price

• High Price

### 📦 Product Physical Features

Created:

• Product Volume

• Product Density

using:

• Length

• Width

• Height

• Weight

measurements.

## 📊 Exploratory Data Analysis

### ⭐ Review Score Analysis

• Examined review score distributions

• Compared review score percentages

• Investigated customer satisfaction patterns

### 💰 Order Value Analysis

• Analyzed total order price distributions

• Evaluated skewness

• Investigated spending behavior

### 📦 Order Characteristics

Compared:

• Freight costs

• Number of items

• Payment values

• Installment counts

### 📊 Order Status Analysis

Analyzed order status frequencies and customer outcomes.

### 🏙️ Customer Location Analysis

Compared average order values across cities.

### 💳 Payment Analysis

Investigated:

• Payment methods

• Installment usage

• Purchasing patterns

### ⭐ Review Score Relationships

Explored whether review scores vary across:

• Payment types

• Order statuses

### 📈 Correlation Analysis

Examined relationships between:

• Prices

• Freight costs

• Payments

• Review scores

### ⏳ Temporal Analysis

Investigated:

• Purchase activity by year

• Delivery performance

• Estimated vs actual delivery dates

### 🛍️ Product Analysis

A separate dataset combining products and order items was analyzed.

### 📦 Product Characteristics

Explored:

• Product dimensions

• Product volume

• Product weight

• Product density

### 🏷️ Product Category Analysis

Identified the most frequently purchased product categories.

### 💰 Price Analysis

Compared:

• Product prices

• Product volumes

• Product descriptions

• Freight costs

### 📈 Product Correlations

Investigated relationships between:

• Product description length and spending

• Freight value and price

## 🤖 Machine Learning

The objective was to predict customer review scores.

### 📉 Multiple Linear Regression

Baseline regression model.

### 🌲 Random Forest Regression

Tree-based ensemble model designed to capture nonlinear relationships.

### 🎯 Support Vector Regression (SVR)

Support Vector Machine model for regression tasks.

### 🔧 Preprocessing Pipeline

A reusable preprocessing pipeline was built using:

Numerical Features

• Median imputation

• Standard scaling

Categorical Features

• Most-frequent imputation

• One-hot encoding

### 📏 Evaluation Metrics

Models were evaluated using:

• R² Score

• Mean Absolute Error (MAE)

• Mean Squared Error (MSE)

## 🔍 Key Insights

### ⭐ Most customers leave positive reviews

Review scores of 4 and 5 account for over 77% of all observations, indicating generally high customer satisfaction.

### 💬 Many customers do not leave written comments

Review titles and review messages contain the highest number of missing values, suggesting that customers often rate purchases without leaving written feedback.

### 💰 Order values are heavily right-skewed

Most purchases involve relatively inexpensive products, while a smaller number of expensive orders create a long right tail.

### 📦 Delivered orders dominate the dataset

The vast majority of orders were successfully delivered, which is expected for a large e-commerce platform.

### ⭐ Delivery performance affects customer satisfaction

Orders delivered after the estimated delivery date tend to receive substantially lower review scores.

### 💳 Payment methods have limited influence

Different payment types show only small differences in:

• Number of purchased items

• Customer review scores

### 📊 Numerical features are weak predictors of review scores

Most numerical variables show little correlation with customer satisfaction.

### 🛍️ Product prices and freight costs are moderately related

More expensive products generally incur higher freight costs, although the relationship is not particularly strong.

### 📦 Larger products tend to belong to higher price categories

Average product volume increases steadily from low-priced to high-priced products.

## 🤖 Machine Learning Results

### 📉 Overall Model Performance

All three regression models performed poorly.

Key observations:

• R² scores remained close to zero

• SVR produced negative R² values

• Models struggled to capture meaningful patterns

### 🎯 Why Performance Was Limited

The available features contain limited predictive information about review scores.

Customer satisfaction is likely influenced by factors not fully captured in the dataset, including:

• Individual customer preferences

• Product expectations

• Seller interactions

• Customer service experiences

### 📏 Error Analysis

Models achieved MAE values close to 1 review point.

Given that review scores range from 1 to 5, this represents a relatively large prediction error.

### 🔮 Future Improvements

Future work could explore:

• Classification models instead of regression

• Sentiment analysis of review comments

• Additional delivery-related features

• Advanced ensemble methods

Because review scores are ordinal categories, a classification approach may be more appropriate than regression.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas numpy matplotlib seaborn scikit-learn joblib
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

• Working with relational datasets

• Merging multiple tables

• Data aggregation techniques

• Datetime feature handling

• Feature engineering

• Exploratory Data Analysis (EDA)

• Customer behavior analysis

• E-commerce analytics

• Building preprocessing pipelines

• Missing value imputation

• Regression modeling

• Model evaluation and comparison

• Saving machine learning pipelines using Joblib

• Extracting business insights from transactional data
