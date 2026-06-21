# 🎵 TikTok Engagement Data Analysis

Exploratory Data Analysis (EDA) and Machine Learning project using a TikTok engagement dataset. This beginner-friendly project investigates how video and account characteristics relate to user interaction metrics such as views, likes, comments, shares, and engagement ratios using Python.

## 📌 Project Overview

The purpose of this project is to analyze TikTok engagement patterns and uncover insights about:

• 📈 Video engagement distributions

• ❤️ Likes per second performance

• ⏱️ Video duration trends

• 📢 Claim vs opinion engagement differences

• ✅ Verified vs non-verified account engagement

• 🔥 Correlations between engagement metrics

• 🤖 Machine learning models for predicting likes

This project focuses on:

• Data cleaning

• Feature engineering

• Exploratory Data Analysis (EDA)

• Statistical analysis

• Data visualization

• Correlation analysis

• Regression modeling

• Residual analysis

## 📂 Dataset

The dataset contains information about TikTok videos and account characteristics, including:

• Video duration

• View count

• Like count

• Comment count

• Share count

• Download count

• Claim status

• Verification status

• Author ban status

The dataset is used to explore how content and account-related variables influence engagement performance.

To note, I completed the project a few years ago and I don't remember the correct Kaggle link from which I downloaded the dataset. The closest dataset I have found that looks similar to mine is [this](https://www.kaggle.com/datasets/yakhyojon/tiktok) one.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• ```🤖 Scikit-learn```

• ```🎨 Seaborn```

• ```🔢 NumPy```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed duplicate rows

• Removed missing values

• Standardized column names

• Removed unnecessary columns

• Converted numerical columns into optimized data types

• Converted categorical variables into category data types

• Set the dataset index column

• Created a new engineered feature: Likes Per Second

## 📊 Exploratory Data Analysis

### ❤️ Likes Per Second Analysis

• Compared likes-per-second performance between:

  o Active accounts
  
  o Under review accounts

• Compared short videos (≤ 30 seconds) against longer videos (> 30 seconds)

• Visualized engagement distributions using histograms

### ⏱️ Video Duration Distribution

• Created histograms showing video duration frequencies

• Calculated average engagement ratios:

  o Like ratio
  
  o Comment ratio
  
  o Share ratio

### 📢 Claim vs Opinion Engagement

• Compared average:

  o Views
  
  o Likes
  
  o Comments

between claim-based and opinion-based videos.

• Visualized differences using bar charts

### ✅ Verified vs Non-Verified Accounts

• Compared engagement distributions using boxplots

• Analyzed differences in:

  o Video views
  
  o Video likes

• Used logarithmic scaling to handle extreme values

### 🔥 Correlation Analysis

• Generated a Pearson correlation heatmap

• Explored relationships between:

  o Views
  
  o Likes
  
  o Shares
  
  o Downloads
  
  o Comments

## 🤖 Machine Learning

### 📉 Linear Regression

A Linear Regression model was trained to predict:

• Video Like Count

using:

• Video View Count

The model was evaluated using:

• R² Score

• Mean Squared Error (MSE)

• Mean Absolute Error (MAE)

Residual analysis was also performed to evaluate prediction quality and model behavior.

## 🔍 Key Insights

### ❤️ Short active-account videos perform best

TikTok videos from active accounts lasting 30 seconds or less generally receive the highest likes per second.

### 📈 Engagement distributions are highly right-skewed

Most videos receive moderate engagement, while a small number achieve extremely large numbers of views and likes.

### 📢 Claim videos significantly outperform opinion videos

Claim-based content receives substantially higher average views, likes, and comments than opinion-based content.

### ✅ Verified accounts show extreme engagement outliers

Some verified accounts generate exceptionally large engagement metrics compared to the majority of creators.

### 🔥 Likes strongly correlate with views, shares, and downloads

Correlation analysis showed strong positive relationships between engagement metrics.

## 🤖 Machine Learning Results

### 📉 Linear Regression Performance

The regression model achieved:

• R² Score: approximately 0.63

• Mean Absolute Error (MAE): approximately 43.6k likes

The results indicate a reasonably strong relationship between video views and likes, though prediction errors increase for highly viral videos.

### 📊 Residual Analysis

Residual plots suggest that the model struggles more with videos receiving extremely high like counts, indicating potential non-linearity and variance increases at larger scales.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```git clone https://github.com/ArKhImede/Data-Science-Portfolio.git```

### 2️⃣ Install dependencies
```pip install pandas matplotlib seaborn scikit-learn numpy```

### 3️⃣ Run Jupyter Notebook
```jupyter notebook```

## 📚 What I Learned

Through this project I practiced:

• Data cleaning and preprocessing

• Feature engineering

• Exploratory Data Analysis (EDA)

• Statistical visualization

• Correlation analysis

• Regression modeling

• Residual analysis

• Machine learning evaluation metrics

• Data storytelling and insight extraction
