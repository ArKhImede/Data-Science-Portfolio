# 🛒 Retail Transactions Data Analysis

Exploratory Data Analysis (EDA) and Machine Learning project using a retail transactions dataset. This beginner project analyzes customer purchasing behavior, spending patterns, promotions, payment methods, seasonal trends, and discount prediction models using Python.

## 📌 Project Overview

The purpose of this project is to analyze retail transaction data and uncover insights about:

• 💳 Spending patterns across payment methods

• 🛍️ Product purchasing trends

• 🏪 Store type performance

• 🎯 Promotion and discount effectiveness

• 📅 Seasonal shopping behavior

• 👥 Customer spending patterns

• 🤖 Machine learning models for discount prediction

This project focuses on:

• Data cleaning

• Feature engineering

• Exploratory Data Analysis (EDA)

• Statistical analysis

• Data visualization

• Classification models

• Customer behavior analysis

• Machine learning pipelines

## 📂 Dataset

The dataset contains information about retail transactions, including:

• Customer names

• Products purchased

• Payment methods

• Store types

• Customer categories

• Promotions

• Seasonal data

• Total items purchased

• Total transaction cost

• Discount application status

• Transaction dates

The dataset is used to explore relationships between customer behavior, promotions, and transaction characteristics.

To note, I completed the project a few years ago and I don't remember the correct Kaggle link from which I downloaded the dataset. The closest dataset I have found that looks similar to mine is [this](https://www.kaggle.com/datasets/prasad22/retail-transactions-dataset) one.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• ```🤖 Scikit-learn```

• ```🔢 NumPy```

• ```🎨 Aquarel```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed duplicate rows

• Removed missing values

• Removed unnecessary columns

• Standardized column names

• Cleaned product name formatting

• Converted categorical columns into category data types

• Optimized numerical column data types

• Converted dates into datetime format

• Extracted:

  o Month
  
  o Day
  
  o Year

from transaction dates.

• Created a new engineered feature: Average Order Value (AOV)

• Split customer names into separate name components

• Converted the target feature into binary numerical values

• Reordered columns to place the target feature at the end

## 📊 Exploratory Data Analysis

### 💳 Spending Across Payment Methods

• Compared:

  o Total spending
  
  o Average spending
  
  o Minimum spending
  
  o Maximum spending

across different payment methods.

• Used logarithmic scaling for visualization clarity

### 🏪 Store Type Performance

• Compared store types using:

  o Average items purchased
  
  o Minimum items purchased
  
  o Maximum items purchased

• Analyzed Average Order Value (AOV) across store categories

### 🛍️ Most Purchased Products

• Identified the top 20 most purchased products

• Visualized product popularity using bar charts

### 📦 Total Items vs Total Spending

• Compared spending distributions between customers purchasing:

  o 5 or fewer items
  
  o More than 5 items

### 🎯 Promotion Effectiveness

• Compared customer behavior under:

  o Buy One Get One promotions
  
  o No promotion
  
  o Discount on selected items

• Analyzed:

  o Total spending
  
  o Total items purchased

### 📅 Seasonal Spending Trends

• Compared average customer spending across:

  o Winter
  
  o Spring
  
  o Summer
  
  o Fall

### 👥 Most Common Names and Surnames

• Identified the most common customer first names and surnames

• Visualized distributions using pie charts

### 💰 Average Customer Spend

• Calculated customer-level Average Order Value

• Compared highest and lowest spending customers

### 🎟️ Discount Sensitivity

• Compared discount application frequencies across customer categories

• Explored whether certain customer groups receive discounts more frequently

### 📦 Seasonal Item Trends

• Analyzed item purchase distributions across seasons

• Used boxplots to visualize differences and outliers

### 📈 Monthly Shopping Trends

• Compared average items purchased across months

• Explored whether shopping behavior changes throughout the year

## 🤖 Machine Learning

### 📉 Logistic Regression

A Logistic Regression model was trained to predict:

• Whether a discount would be applied

using features such as:

• Payment method

• Store type

• Customer category

• Seasonal information

• Total transaction cost

• Total items purchased

The project included:

• Feature scaling

• One-hot encoding

• Pipeline preprocessing

The model was evaluated using:

• Accuracy

• Precision

• Recall

• F1 Score

### 🌲 Random Forest Classification

A Random Forest Classifier was trained using the same preprocessing pipeline and features.

The project compared Random Forest performance against Logistic Regression to evaluate whether ensemble learning improved predictive accuracy.

## 🔍 Key Insights

### 💳 Payment methods show very similar spending behavior

Total, average, minimum, and maximum spending values were nearly identical across all payment methods.

### 🏪 Store types perform similarly

Store categories showed only small differences in:

• Items purchased

• Average Order Value (AOV)

### 🛍️ Common grocery products dominate purchases

Products such as toothpaste, yogurt, and milk appeared among the most purchased items.

### 🎯 Promotions do not strongly affect customer behavior

Promotions showed little meaningful impact on:

• Total spending

• Number of items purchased

### 📅 Seasonal trends remain stable

Average spending and item purchases stayed relatively constant across seasons and months.

### 👥 Discount application appears balanced

Discounts were applied almost equally across customer categories, suggesting limited underlying patterns.

## 🤖 Machine Learning Results

### 📉 Logistic Regression Performance

The Logistic Regression model achieved:

• Accuracy: approximately 0.50

• Precision: approximately 0.49

• Recall: approximately 0.44

The model struggled to identify meaningful predictive relationships between customer features and discount application.

### 🌲 Random Forest Classification Performance

The Random Forest Classifier achieved:

• Accuracy: approximately 0.51

• Precision: approximately 0.51

• Recall: approximately 0.48

Although Random Forest slightly outperformed Logistic Regression, the improvement was minimal.

### ⚠️ Interpretation

The weak performance across all evaluation metrics suggests that:

• The dataset likely contains limited predictive relationships

• Many variables appear evenly distributed

• The dataset may contain synthetic or artificially balanced patterns

As a result, the models struggled to learn strong classification signals.

## ⚠️ Dataset Limitations

Several limitations should be considered:

• Many variables appear artificially balanced

• Promotions and customer categories show limited variation

• Seasonal behavior remains unusually stable

• The dataset may contain synthetic transaction patterns

Because of this, the project is best suited for practicing:

• Data analysis

• Visualization

• Feature engineering

• Machine learning pipelines

• Classification modeling

rather than drawing real-world retail business conclusions.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib scikit-learn aquarel numpy
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

• Customer behavior analysis

• Classification modeling

• Logistic Regression

• Random Forest Classification

• Machine learning pipelines

• Model evaluation metrics
