# 🎵 Spotify Tracks Analysis & Popularity Prediction

Exploratory Data Analysis (EDA) and Machine Learning project using the Spotify Tracks dataset. This beginner-friendly project explores Spotify audio features, popularity trends, artist statistics, and predictive modeling using Python, Pandas, Matplotlib, and Scikit-learn.

## 📌 Project Overview

The purpose of this project is to analyze Spotify tracks and uncover insights about:

• 🎧 Audio features and popularity

• 🔊 Relationships between audio characteristics

• 📈 Popularity and tempo distributions

• 🔞 Explicit vs non-explicit songs

• 🎤 Most common artists

• 🎼 Genre distributions

• 🤖 Machine learning models for popularity prediction

This project focuses on:

• Data cleaning

• Data transformation

• Exploratory Data Analysis (EDA)

• Statistical analysis

• Machine Learning

• Data visualization

## 📂 Dataset

The dataset contains information about Spotify tracks, including:

• Track name

• Artist(s)

• Album name

• Popularity score

• Genre

• Explicit status

• Danceability

• Energy

• Loudness

• Acousticness

• Tempo

• Valence

• Speechiness

• Instrumentalness

• Liveness

You can use this (link)[https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset] to download the dataset.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• 🔢 ```NumPy```

• 🤖 ```Scikit-learn```

• 🎨 ```Catppuccin```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed unnecessary columns

• Removed duplicate rows

• Handled missing values

• Renamed columns for readability

• Split artists into separate rows

• Created a separate dataframe for artist analysis

## 📊 Exploratory Data Analysis

### 🎧 Popularity Analysis

• Explored correlations between popularity and audio features

• Created a feature correlation heatmap

### 🔊 Audio Feature Relationship Analysis

• Analyzed the relationship between Energy and Loudness

• Explored the relationship between Acousticness and Energy

### 📈 Distribution Analysis

• Analyzed tempo distribution

• Explored popularity distribution and skewness

• Compared mean and median values

### 🔞 Explicit vs Non-Explicit Songs

• Compared average popularity

• Compared average energy levels

### 🎤 Artist Analysis

• Identified artists dominating highly popular tracks

• Found artists with the highest number of songs

### 🎼 Genre Analysis

• Explored genre distributions

• Compared the most common genres

## 🤖 Machine Learning Models

### 📉 Multiple Linear Regression

• Predicted popularity using numerical audio features

• Evaluated performance using:
  o Mean Absolute Error (MAE)
  
  o R² Score

### 🌲 Random Forest Regressor

• Built a Random Forest model to improve prediction accuracy

• Compared results against linear regression

## 🔍 Key Insights

### 🎧 Popularity has weak linear correlations

Most individual audio features showed weak direct correlations with popularity.

### 🔊 Energy and loudness are strongly correlated

Energy and loudness showed a strong positive correlation.

### 📈 Tempo distribution is nearly normal

Tempo values are centered around approximately 122 BPM.

### 📉 Popularity is right-skewed

Most songs have moderate popularity, while fewer tracks achieve extremely high popularity.

### 🔞 Explicit songs tend to perform better

Explicit songs are, on average:

• More popular

• More energetic

### 🎤 Artist observations

• Bad Bunny appeared most frequently in the dataset

• J Balvin had the highest number of songs

### 🎼 Genre distribution is balanced

No genre overwhelmingly dominated the dataset, suggesting balanced sampling.

### 🤖 Random Forest outperformed Linear Regression

Random Forest achieved:

• Lower Mean Absolute Error

• Higher R² Score

The Multiple Linear Regression model underfit the data due to high bias.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```git clone https://github.com/ArKhImede/Data-Science-Portfolio.git```

### 2️⃣ Install dependencies
```pip install pandas matplotlib numpy scikit-learn catppuccin```

### 3️⃣ Run Jupyter Notebook
```jupyter notebook```

## 📚 What I Learned

Through this project I practiced:

• Data cleaning and preprocessing

• Correlation analysis

• Statistical analysis

• Data visualization

• Machine learning regression models

• Model evaluation using MAE and R² Score
