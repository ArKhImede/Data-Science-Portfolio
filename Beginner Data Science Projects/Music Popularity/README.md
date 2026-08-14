# 🎵 Music Popularity Data Analysis

Exploratory Data Analysis (EDA) and Machine Learning project using a global music dataset. This beginner project investigates how musical characteristics such as danceability, energy, loudness, duration, and acousticness relate to track popularity using Python.

## 📌 Project Overview

The purpose of this project is to analyze music track characteristics and uncover insights about:

• 🎤 Artist popularity trends

• 📈 Track popularity over time

• 🎶 Danceability vs acousticness relationships

• ⚡ Energy patterns in music

• 📅 Release date popularity trends

• 🔥 Correlations between audio features

• 🤖 Machine learning models for predicting popularity

This project focuses on:

• Data cleaning

• Feature engineering

• Exploratory Data Analysis (EDA)

• Statistical analysis

• Data visualization

• Correlation analysis

• Regression modeling

• Feature importance analysis

## 📂 Dataset

The dataset contains information about globally popular music tracks, including:

• Track name

• Artist name

• Album name

• Popularity score

• Danceability

• Acousticness

• Energy

• Loudness

• Tempo

• Duration

• Speechiness

• Instrumentalness

• Liveness

• Musical mode

• Release date

• Country and market information

The dataset is used to explore relationships between musical attributes and track popularity.

To note, I completed the project a few years ago and I don't remember the correct Kaggle link from which I downloaded the dataset. The closest dataset I have found that looks similar to mine is [this](https://www.kaggle.com/datasets/miquelneck/worlds-spotify-top-50-playlist-musicality-data) one.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• ```🤖 Scikit-learn```

• ```🔢 NumPy```

• ```🎨 Seaborn```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed duplicate rows

• Removed missing values

• Removed unnecessary columns

• Renamed inconsistent column names

• Converted numerical columns into optimized data types

• Converted categorical columns into category data types

• Converted date columns into datetime format

• Extracted:

  o Year
  
  o Month
  
  o Day

from release dates.

• Created a new engineered feature: Track Name Length

• Reordered columns to place the target feature at the end

## 📊 Exploratory Data Analysis

### 🎤 Top Artists by Popularity

• Calculated average popularity scores for artists

• Visualized the top 10 most popular artists using horizontal bar charts

### 📅 Popularity Trends Over Time

• Compared average popularity:

  o By year
  
  o By month
  
  o By day

• Explored how release timing may influence popularity

### 🎶 Danceability vs Acousticness

• Created scatter plots comparing:

  o Average danceability
  
  o Average acousticness

by country.

• Observed moderate negative relationships between the two features

### 📊 Popularity Statistics

• Generated descriptive statistics for popularity metrics

• Visualized statistical distributions using bar charts

### ⚡ Albums with the Highest Energy

• Compared album-level average energy values

• Identified the most energetic albums in the dataset

### 🔥 Danceability vs Energy by Popularity

• Built scatter plots colored by popularity values

• Explored how highly danceable and energetic tracks relate to popularity

### 📈 Track Releases Over Time

• Analyzed yearly track release counts

• Observed strong concentration of tracks in recent years

### 📝 Track Name Length vs Popularity

• Explored whether longer track names influence popularity

• Found no meaningful relationship

### 🎼 Energy by Musical Mode

• Compared energy distributions between:

  o Major mode songs
  
  o Minor mode songs

using boxplots.

### 🔥 Correlation Analysis

• Generated a Pearson correlation heatmap

• Explored relationships between numerical musical features

## 🤖 Machine Learning Models

### 📉 Multiple Linear Regression

A Multiple Linear Regression model was trained to predict:

• Track Popularity

using numerical audio features such as:

• Danceability

• Energy

• Loudness

• Tempo

• Duration

• Acousticness

The model was evaluated using:

• R² Score

• Mean Absolute Error (MAE)

Residual analysis was also performed to evaluate prediction quality.

### 🌲 Random Forest Regression

A Random Forest Regressor was trained using the same numerical features to improve prediction performance.

The project also included:

• Feature importance analysis

• Residual analysis

• Comparison against linear regression performance

## 🔍 Key Insights

### 🎤 Certain artists dominate popularity rankings

Artists such as Tate McRae, Iñigo Quintero and Kenya Grace achieved some of the highest average popularity scores in the dataset.

### 🎶 Danceability and acousticness show a negative relationship

Tracks with higher danceability generally tend to have lower acousticness values.

### ⚡ Highly energetic albums stand out

Albums such as UTA’S SONGS ONE PIECE FILM RED showed exceptionally high energy values.

### 📈 The dataset is heavily concentrated in recent years

Most tracks were released in 2023, making long-term trend analysis less reliable.

### 📝 Track name length does not affect popularity

No meaningful relationship was found between title length and popularity scores.

### 🎼 Major and minor songs show similar energy distributions

Both modes contain low-energy outliers while most tracks cluster around higher energy levels.

## 🤖 Machine Learning Results

### 📉 Multiple Linear Regression Performance

The linear regression model achieved:

• Test R² Score: approximately 0.05

• Train R² Score: approximately 0.07

• Mean Absolute Error (MAE): approximately 12.29 popularity points

The results indicate that linear regression underfits the data and struggles to capture complex relationships between musical features and popularity.

### 🌲 Random Forest Regression Performance

The Random Forest Regressor achieved stronger results:

• Train R² Score: approximately 0.96

• Test R² Score: approximately 0.68

• Mean Absolute Error (MAE): approximately 4.96 popularity points

The model demonstrated significantly better predictive performance, although the large gap between training and testing performance suggests overfitting.

### 🔥 Most Important Features

Feature importance analysis suggested that the strongest popularity predictors included:

• Duration

• Danceability

• Loudness

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib seaborn scikit-learn numpy
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

• Correlation analysis

• Multiple Linear Regression

• Random Forest Regression

• Residual analysis

• Feature importance analysis

• Machine learning evaluation metrics
