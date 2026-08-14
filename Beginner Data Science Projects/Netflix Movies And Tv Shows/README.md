# 🎬 Netflix Content Data Analysis

Exploratory Data Analysis (EDA) project using the Netflix titles dataset. This beginner-friendly project analyzes Netflix’s catalog to uncover trends related to movies, TV shows, genres, ratings, countries, directors, and content growth over time using Python.

## 📌 Project Overview

The purpose of this project is to analyze Netflix content and uncover insights about:

• 🎥 Movies vs TV show distributions

• 📈 Netflix catalog growth over time

• 🌍 Country-level content production

• 🎭 Genre popularity trends

• 🔞 Audience rating distributions

• ⏱️ Movie and TV show duration patterns

• 🎬 Director activity and content creation

• 📊 International content expansion

This project focuses on:

• Data cleaning

• Feature engineering

• Exploratory Data Analysis (EDA)

• Statistical analysis

• Data visualization

• Content trend analysis

• Audience segmentation

## 📂 Dataset

The dataset contains information about Netflix titles, including:

• Title names

• Type (Movie or TV Show)

• Directors

• Cast members

• Countries

• Release years

• Ratings

• Duration

• Genres

• Date added to Netflix

• Descriptions

The dataset is used to explore how Netflix’s content catalog evolved over time and how different countries, genres, and audience categories contribute to the platform.

You can use this [link](https://www.kaggle.com/datasets/shivamb/netflix-shows) to download the dataset.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Standardized column names

• Removed unnecessary whitespace from text columns

• Converted date columns into datetime format

• Extracted numerical duration values from text fields

• Created audience rating categories:

  o Kids
  
  o Teens
  
  o Adults

• Split and exploded multi-value columns such as:

  o Countries
  
  o Genres
  
  o Directors

to improve analysis.

• Created new engineered features such as:

  o Duration numbers
  
  o Rating categories

## 📊 Exploratory Data Analysis

### 🎥 Movies vs TV Shows

• Compared the distribution of:

  o Movies
  
  o TV Shows

• Visualized percentage distributions using pie charts

### 📈 Content Growth Over Time

• Analyzed release growth by year

• Identified years with the largest number of releases

• Compared growth trends for movies and TV shows after 2005

### 🌍 Country Analysis

• Identified the top countries producing Netflix content

• Compared movie-focused and TV-focused countries

• Visualized international production trends

### 🔞 Ratings Analysis

• Analyzed the distribution of Netflix ratings such as:

  o TV-MA
  
  o TV-14
  
  o PG-13
  
  o TV-PG

• Grouped ratings into broader audience categories:

  o Kids
  
  o Teens
  
  o Adults

### ⏱️ Duration Analysis

• Compared:

  o Average movie duration
  
  o Minimum movie duration
  
  o Maximum movie duration

• Compared TV show season statistics

### 🎭 Genre Analysis

• Identified the most common Netflix genres

• Compared popularity of:

  o Dramas
  
  o Comedies
  
  o International movies

### 🎬 Director Analysis

• Identified directors with the highest number of titles

• Explored directors working on both movies and TV shows

### 🌍 Content Growth by Country

• Compared long-term content growth trends between:

  o United States
  
  o India

using line plots and filled area visualizations.

## 🔍 Key Insights

### 🎥 Movies dominate Netflix’s catalog

Movies represent approximately 70% of the dataset, while TV shows make up the remaining 30%.

### 📈 Netflix expanded rapidly after 2005

The number of releases increased significantly between 2016 and 2020, reflecting Netflix’s global expansion strategy.

### 🌍 The United States leads content production

The United States appears most frequently as a production country and dominates both movie and TV show counts.

### 🇮🇳 India is a major movie producer

India ranks second in movie production counts within the dataset.

### 🔞 Netflix primarily targets teen and adult audiences

TV-MA and TV-14 are the most common ratings, while children’s content represents a smaller share of the catalog.

### ⏱️ Movies average around 100 minutes

TV shows average approximately two seasons in duration.

### 🎭 Dramas and international content are highly common

International movies, dramas, and comedies are among the most frequently appearing genres.

### 🎬 Certain directors appear repeatedly

Directors such as Youssef Chahine, Cathy Garcia-Molina, and Martin Scorsese appear frequently throughout the dataset.

## ⚠️ Dataset Limitations

Several limitations should be considered:

• Some titles contain missing metadata

• Multi-country and multi-genre titles can inflate category counts after exploding columns

• The dataset reflects Netflix catalog availability rather than audience viewing behavior

• Content counts do not directly measure popularity or streaming success

Because of this, the project is best suited for practicing:

• Data cleaning

• Feature engineering

• Visualization

• Exploratory Data Analysis

• Trend analysis

rather than drawing exact business conclusions about Netflix viewership.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

## 📚 What I Learned

Through this project I practiced:

• Data cleaning and preprocessing

• Handling missing values

• Datetime manipulation

• Exploding multi-value categorical columns

• Exploratory Data Analysis (EDA)

• Statistical visualization

• Trend analysis

• Audience segmentation

• Content distribution analysis
