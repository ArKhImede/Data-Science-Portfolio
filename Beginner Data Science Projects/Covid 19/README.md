# 🦠 Covid 19 

Exploratory Data Analysis (EDA) and Machine Learning project using a global COVID-19 dataset. This project analyzes worldwide pandemic statistics, growth patterns, fatality rates, and regional differences using Python, Pandas, Matplotlib, NumPy, and Scikit-learn.

## 📌 Project Overview

The purpose of this project is to analyze COVID-19 data and uncover insights about:

• 🧪 Case fatality rates across countries and WHO regions

• 📈 Infection growth trends and doubling times

• 🌍 Regional comparisons of deaths, recoveries, and active cases

• 🔥 Correlation between confirmed cases and weekly increases

• ⚠️ Outlier detection in pandemic statistics

• 🤖 Machine Learning clustering and classification

This project focuses on:

• Data cleaning

• Feature engineering

• Exploratory Data Analysis (EDA)

• Data visualization

• Statistical analysis

• Machine Learning with Scikit-learn

## 📂 Dataset

The dataset contains worldwide COVID-19 statistics, including:

• Country/Region

• Confirmed Cases
  
• Deaths
  
• Recovered Cases
  
• Active Cases
  
• New Cases
  
• New Deaths
  
• New Recovered
  
• WHO Region
  
• Weekly Growth Metrics

To note, I completed the project a few years ago and I don't remember the correct Kaggle link from which I downloaded the dataset. The closest dataset I have found that looks similar to mine is [this](https://www.kaggle.com/datasets/imdevskp/corona-virus-report) one.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```🔢 NumPy```

•	```📈 SciPy```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• ```🤖 Scikit-learn```

• ```🎨 Aquarel```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed missing values

• Renamed columns for readability

• Set country names as dataframe index

• Converted WHO Region to categorical data type

• Removed infinite values from calculations

• Created new analytical features:

  • Case Fatality Rate
  
  • Case Fatality Rate %
  
  • Growth Factor
  
  • Exponential Growth Rate (r)
  
  • Doubling Time

## 📊 Exploratory Data Analysis

### 🧪 Case Fatality Rate (CFR)

• Identified countries with the highest fatality rates

• Compared average CFR across WHO regions

• Visualized top countries by CFR percentage

### 📈 Doubling Time Analysis

• Calculated doubling times using exponential growth formulas

• Compared countries with the fastest and slowest spread rates

• Visualized doubling time distributions

### 🌍 Confirmed Cases vs Weekly Increase

• Analyzed the relationship between total confirmed cases and 1-week percentage increases

• Investigated whether highly infected countries still experienced rapid growth

### 🏥 WHO Region Metrics

Compared regional averages for:

• Deaths

• Recoveries

• Active Cases

### 🔵 Bubble Chart Analysis

Visualized:

• Confirmed Cases

• Deaths Per 100 Cases

• Total Death Counts

using bubble charts for multidimensional analysis.

### 🔥 Correlation Analysis

• Created a correlation heatmap between numerical COVID-19 metrics

• Identified strong and weak relationships between features

### ⚠️ Outlier Detection

• Used z-score analysis to detect abnormal countries in:

  • Deaths Per 100 Recovered

## 🤖 Machine Learning

### 🔹 K-Means Clustering

Used:

• Confirmed Cases

• 1-week % Increase

to group countries into clusters based on pandemic behavior.

**Findings:**

• Most countries formed a low-to-medium growth cluster

• Some countries appeared as outliers with:

  • Extremely high confirmed cases
  • Extremely high weekly growth

### 🌲 Random Forest Classification

Built a Random Forest Classifier to predict:

• WHO Region

using features such as:

• Confirmed Cases

• Active Cases

• Recoveries

• New Cases

• New Deaths

• New Recoveries

• Model Evaluation

Used:

• Accuracy Score

• Precision

• Recall

• F1 Score

• Confusion Matrix

• GridSearchCV for hyperparameter tuning

## 🔍 Key Insights

### 🧪 Highest Fatality Rates

• Yemen showed the highest case fatality rate

• Europe had the highest average WHO regional CFR

### 📈 Growth Trends

• Countries with the largest confirmed cases did not necessarily have the highest weekly growth percentages

• Smaller countries sometimes showed extremely high short-term growth

### 🌍 Regional Differences

• Americas had the highest total deaths, recoveries, and active cases

• Highly populated regions dominated absolute counts

### ⚠️ Outliers Exist

Several countries behaved as statistical outliers in terms of:

• Weekly growth

• Fatality rates

• Recovery ratios

## 🤖 Machine Learning Results

### K-Means

• Successfully separated countries into distinct pandemic behavior groups

### Random Forest

• Performed reasonably well for Europe and Africa

• Struggled with smaller WHO regions due to dataset imbalance

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib scipy numpy scikit-learn aquarel
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

## 📚 What I Learned

Through this project I practiced:

• Data cleaning with Pandas

• Feature engineering

• Statistical analysis

• Data visualization with Matplotlib

• Correlation analysis

• Outlier detection using z-scores

• K-Means clustering

• Random Forest classification

• Hyperparameter tuning with GridSearchCV

• Extracting insights from real-world health datasets
