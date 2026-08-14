# ⚔️ Attack on Titan Reviews Analysis

Exploratory Data Analysis (EDA) and Machine Learning project using an Attack on Titan reviews dataset. This beginner-friendly project explores review engagement, voting behavior, review length patterns, seasonality trends, and clustering analysis using Python.

## 📌 Project Overview

The purpose of this project is to analyze Attack on Titan user reviews and uncover insights about:

• 👍 Upvotes vs downvotes

• 📈 Review engagement trends over time

• ✍️ Review length and popularity

• 🗓️ Monthly review activity

• 🔥 Most frequent words in reviews

• 📊 Voting patterns and seasonality

• 🤖 Machine learning models for upvote prediction

• 🎯 Clustering user engagement patterns

This project focuses on:

• Data cleaning

• Data transformation

• Exploratory Data Analysis (EDA)

• Statistical analysis

• Machine Learning

• Data visualization

## 📂 Dataset

The dataset contains user reviews related to the anime Attack on Titan, including:

• Review title

• Full review comment

• Rating

• Upvotes

• Downvotes

• Review date

The dataset includes over 2000 reviews collected between 2013 and 2025.

To note, I completed the project a few years ago and I don't remember the correct Kaggle link from which I downloaded the dataset. The closest dataset I have found that looks similar to mine is [this](https://www.kaggle.com/datasets/karimabenzahra/attack-on-titan-imdb-reviews-dataset) one.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• ```🔢 NumPy```

• ```🤖 Scikit-learn```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed invalid rows

• Removed duplicate or unnecessary entries

• Converted string-based numeric values:

  o Upvotes
  
  o Downvotes

into numeric format.

• Converted review dates into:

  o Month
  
  o Day
  
  o Year

• Created new engineered features:

  o Review Length
  
  o Review Length Category
  
  o Comment Word Count

• Categorized reviews into:

  o Short
  
  o Medium
  
  o Long

## 📊 Exploratory Data Analysis

### 👍 Upvotes vs Downvotes Analysis

• Compared upvote and downvote distributions

• Calculated average upvote ratio per comment

### 📈 Time Trend Analysis

• Explored upvote trends between 2013 and 2025

• Compared yearly engagement patterns

### ✍️ Review Length Analysis

• Investigated whether longer reviews receive more upvotes

• Compared engagement between:
  o Short reviews
  
  o Medium reviews
  
  o Long reviews

### 🔥 Most Frequent Words

• Identified the most common words used in review titles

### 🗓️ Monthly Review Activity

• Analyzed review frequency by month

• Explored seasonality patterns in review activity

### 📊 Seasonality Heatmap

• Created a heatmap of average upvotes by:

  o Month
  
  o Year

### 📈 Cumulative Popularity Analysis

• Compared cumulative upvotes across multiple years

### 👍👎 Vote Ratio Evolution

• Compared total upvotes and downvotes over time

## 🤖 Machine Learning

### 📉 Multiple Linear Regression

A Multiple Linear Regression model was trained to predict upvotes using:

• Review year

• Comment word count

Model evaluation metrics included:

• Mean Absolute Error (MAE)

• R² Score

### 🎯 K-Means Clustering

K-Means clustering was used to identify different engagement patterns based on:

• Upvotes

• Downvotes

The elbow method was used to determine the optimal number of clusters.

## 🔍 Key Insights

### 👍 Reviews receive overwhelmingly positive engagement

The average upvote ratio per comment was approximately 81%, indicating strongly positive community reactions.

### 📈 Engagement peaked around 2021

The largest amount of engagement occurred during the anime’s peak popularity years.

### ✍️ Longer reviews do not guarantee more upvotes

Medium-length reviews often performed similarly or better than longer reviews.

### 🔥 Fans strongly praise the series

The most common review words included:

• “Masterpiece”

• “Amazing”

• “The best”

This aligns with the fact that most users rated the anime very highly.

### 🗓️ Most reviews occur early in the year

January and February contained the largest share of reviews in the dataset.

### 📊 Upvotes increased significantly during major release periods

Years such as 2019 and 2021 showed major spikes in engagement.

## 🤖 Machine Learning Results

### 📉 Multiple Linear Regression Performance

The model achieved:

• Mean Absolute Error (MAE): 13.9

• R² Score: 0.10

The low R² score suggests that review year and comment length alone are not sufficient to explain engagement patterns.

### 🎯 K-Means Clustering Insights

The clustering model identified five major engagement groups:

• Low-engagement comments

• Medium-engagement comments

• High-engagement comments

• Highly controversial comments

• Outlier comments with extremely high vote counts

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib numpy scikit-learn
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

## 📚 What I Learned

Through this project I practiced:

• Data cleaning and preprocessing

• Feature engineering

• Working with datetime data

• Statistical analysis

• Data visualization

• Machine learning regression models

• K-Means clustering

• Model evaluation using MAE and R² Score

•	Extracting insights from real-world datasets
