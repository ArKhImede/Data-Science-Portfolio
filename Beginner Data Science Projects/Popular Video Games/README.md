# 🎮 Popular Video Games Analysis (1980–2023)

Exploratory Data Analysis (EDA) and Machine Learning project using a dataset of popular video games released between 1980 and 2023. This beginner-friendly project explores video game ratings, genres, release trends, player engagement, and predictive modeling using Python.

## 📌 Project Overview

The purpose of this project is to analyze popular video games and uncover insights about:

• 🎮 Top-rated games

• 🏢 Most successful studios

• 🎭 Most common game genres

• 📈 Game release trends over time

• ⭐ Rating distributions

• 🎯 Relationships between ratings, plays, and wishlists

• 📚 Backlog trends

• 🤖 Machine learning models for rating prediction

This project focuses on:

• Data cleaning

• Data transformation

• Exploratory Data Analysis (EDA)

• Statistical analysis

• Machine Learning

• Data visualization

## 📂 Dataset

The dataset contains information about popular video games, including:

• Title

• Release Date

• Rating

• Number of Reviews

• Plays

• Playing

• Backlogs

• Wishlist counts

• Genres

• Development studios

The dataset covers games released between 1980 and 2023.

You can use this [link](https://www.kaggle.com/datasets/arnabchaki/popular-video-games-1980-2023) to download the dataset.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• ```🔢 SciPy```

• ```🤖 Scikit-learn```

• ```🎨 Aquarel```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Removed missing values

• Removed duplicate game titles

• Dropped unnecessary columns

• Converted release dates to datetime format

• Extracted release years

• Converted string values such as:
  o Plays
  
  o Wishlists
  
  o Reviews
  
  o Backlogs

into numeric values.

• Split multi-value columns:
  o Genres
  
  o Development studios

• Created separate dataframes for:
  o Genres analysis
  
  o Studio analysis

## 📊 Exploratory Data Analysis

### 🎮 Top Rated Games

• Identified the highest-rated games in the dataset

• Explored studios appearing most frequently among highly rated titles

### 🎭 Genre Analysis

• Explored the most common genres

• Compared genre popularity

• Investigated whether RPGs dominate the dataset

### ⭐ Rating Distribution

• Analyzed rating distribution

• Measured skewness using statistical analysis

### 📈 Game Releases Over Time

• Identified years with the highest number of releases

• Explored release trends after 2010

### 🎯 Correlation Analysis

• Analyzed relationships between:
  o Ratings and plays
  
  o Ratings and wishlists

### 🎮 Most Played Games

• Identified games with the highest play counts

• Compared popularity and ratings

### 📚 Backlog Analysis

• Explored games with the largest backlog counts

• Investigated whether RPGs tend to accumulate larger backlogs

### 🎭 Genre vs Rating Analysis

• Compared average ratings between genres

• Explored whether indie or niche genres receive higher ratings

## 🤖 Machine Learning Models

### 📉 Linear Regression Model

A Linear Regression model was trained to predict game ratings using:

• Plays

• Wishlist counts

• Backlogs

• Number of Reviews

• Times Listed

Model evaluation metrics included:

• Mean Absolute Error (MAE)

• R² Score

## 🔍 Key Insights

### 🎮 Highest-rated games

The highest-rated games include:

• Elden Ring

• Tokyo Necro

• Disco Elysium

• Bloodborne

• Outer Wilds

### 🎭 Adventure games dominate

Adventure games are the most common genre, followed by RPGs.

### ⭐ Ratings are left-skewed

Most games received relatively high ratings, resulting in a negatively skewed distribution.

### 📈 Releases increased significantly after 2010

Game releases have steadily increased over the past decade, with 2022 having the highest number of releases.

### 🎯 Highly rated games do not always dominate plays

Ratings showed only a weak correlation with play counts. Wishlist counts showed a stronger relationship with ratings than plays did.

### 🎮 Popularity does not guarantee high ratings

Some highly played games, such as GTA V and Among Us, do not have the highest ratings in the dataset.

### 📚 RPGs accumulate the largest backlogs

RPG titles tend to have the highest average backlog counts, likely due to their long completion times.

### 🎭 Genre ratings vary significantly

Among sufficiently represented genres:

• MOBA games had the lowest average ratings

• Visual Novels achieved the highest average ratings

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib scipy scikit-learn aquarel
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

## 📚 What I Learned

Through this project I practiced:

• Data cleaning and preprocessing

• Working with datetime data

• Statistical analysis using SciPy

• Correlation analysis

• Data visualization

• Feature engineering

• Machine learning regression models

• Model evaluation using MAE and R² Score
