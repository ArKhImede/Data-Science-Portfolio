# 🏙️ Chicago Community Area Segmentation

Exploratory Data Analysis (EDA), Feature Engineering, Data Integration, and Unsupervised Machine Learning project using Chicago Census, Public Schools, and Crime datasets. This project combines multiple public datasets to analyze socioeconomic conditions, education quality, and crime across Chicago community areas, ultimately identifying meaningful community profiles through K-Means clustering.

## 📌 Project Overview

The purpose of this project is to integrate multiple public datasets and uncover insights about:

• 🏙️ Community socioeconomic conditions

• 🎓 Public school quality

• 🚔 Crime patterns

• 💰 Income distribution

• 📉 Poverty and unemployment

• 🏘️ Housing conditions

• 🤖 Unsupervised machine learning

• 📊 Community segmentation

This project focuses on:

• Data cleaning

• Data integration

• Feature engineering

• Exploratory Data Analysis (EDA)

• Correlation analysis

• Outlier detection

• Feature selection

• K-Means clustering

• Cluster interpretation

## 📂 Dataset

The project combines three public datasets:

• Chicago Census Data

• Chicago Public Schools Data

• Chicago Crime Data

After cleaning and aggregation, each row represents a single Chicago community area.

The merged dataset contains information about:

• Socioeconomic indicators

• Public school performance

• Crime statistics

• Community characteristics

You can use this [link](https://www.kaggle.com/datasets/kanzariachref/chicago-crime-public-schools-and-census-data?select=ChicagoPublicSchools.csv) to download the dataset.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```🔢 NumPy```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```🤖 Scikit-learn```

• ```🗂️ PyArrow```

• ```📓 Jupyter Notebook```

• ```🎨 Catppuccin```

## 🧹 Data Cleaning

The three datasets were cleaned independently before being merged.

Cleaning steps included:

• Removed duplicate records

• Handled missing values

• Replaced invalid values (e.g. "NDA")

• Converted percentage columns into numeric values

• Optimized data types

• Removed unnecessary columns

• Aggregated school statistics by community area

• Aggregated crime statistics by community area

• Merged census, education, and crime datasets

• Imputed missing school quality metrics using median values

• Filled missing crime statistics with zero where appropriate

• Verified the final merged dataset contained no duplicates or missing values

## ⚙️ Feature Engineering

Several features were created to better describe each community area.

### 🎓 Education Features

• School Quality Score

Average of:

• Safety Score

• Family Involvement Score

• Environment Score

• Instruction Score

### 🚔 Crime Features

• Crimes Per Income

Crime count relative to community income.

• Crimes Per Crime Category

Average crime count across distinct crime categories.

• Arrests Per Crime

Proportion of crimes resulting in arrests.

These engineered variables were primarily used during exploratory analysis. To reduce redundancy, they were excluded from the final clustering model.

## 📊 Exploratory Data Analysis

### 📈 Distribution Analysis

• Examined crime distributions

• Evaluated school quality distributions

• Investigated arrest rates

• Checked feature skewness

### 🏙️ Community Analysis

• Compared hardship across communities

• Identified highest- and lowest-income areas

• Compared school quality between communities

• Investigated crime in disadvantaged areas

### 📉 Correlation Analysis

• Examined correlations between socioeconomic variables

• Identified variables strongly associated with hardship

• Investigated relationships between crime and education

### 🚨 Outlier Analysis

• Identified crime outliers using the IQR method

• Evaluated highly skewed variables for later preprocessing

## 🔍 Key Insights

### 🚔 Crime is highly concentrated

Crime counts are strongly right-skewed, with a small number of community areas experiencing substantially more crime than the majority.

### 📉 Higher hardship areas experience more crime

Communities with higher hardship indices generally exhibit higher average crime counts.

### 🎓 Wealthier communities tend to have stronger school performance

Higher-income areas generally achieve higher school safety and family involvement scores while experiencing lower crime levels.

### 💰 Socioeconomic variables are strongly correlated

Poverty, unemployment, housing crowding, and educational attainment are all strongly associated with hardship.

### 🏫 Teaching quality appears relatively consistent

Little difference was observed in average teaching quality between the lowest- and highest-income communities.

## 🤖 Community Segmentation

K-Means clustering was used to identify groups of community areas with similar socioeconomic characteristics.

### 🔧 Data Preparation

Before clustering:

• Removed identifier columns

• Removed redundant engineered variables

• Applied log transformations to highly skewed features

• Standardized all numerical variables using ```StandardScaler```

### 📏 Cluster Selection

The optimal number of clusters was determined using:

• Elbow Method

• Silhouette Analysis

### 🎯 Clustering Features

The clustering model included:

• Housing crowding

• Poverty

• Unemployment

• Educational attainment

• Age demographics

• Per-capita income

• School quality metrics

• Student attendance

• Crime statistics

## 🏆 Community Profiles

### 🔹 Cluster 0 — Economically Disadvantaged Communities

Characteristics:

• Higher poverty

• Higher unemployment

• More crowded housing

• Lower income

• Lower school safety

• Lower family involvement

• Higher crime rates

• Lower student attendance

These communities represent areas facing greater socioeconomic challenges.

### 🔸 Cluster 1 — More Affluent Communities

Characteristics:

• Higher per-capita income

• Lower poverty

• Lower unemployment

• Better school quality

• Higher safety scores

• Lower crime rates

• Higher student attendance

These communities represent more economically advantaged areas with stronger educational outcomes.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```git clone https://github.com/ArKhImede/Data-Science-Portfolio.git```

### 2️⃣ Install dependencies
```pip install pandas numpy matplotlib seaborn scikit-learn pyarrow catppuccin```

### 3️⃣ Run Jupyter Notebook
```jupyter notebook```

Run the notebooks in the following order:

1. cleaning.ipynb

2. feature_engineering.ipynb

3. EDA.ipynb

4. train_and_evaluate.ipynb

## 📚 What I Learned

Through this project I practiced:

• Data integration from multiple sources

• Data aggregation

• Feature engineering

• Exploratory Data Analysis (EDA)

• Correlation analysis

• Outlier detection

• Feature selection

• Working with public datasets

• Unsupervised machine learning

• K-Means clustering

• Cluster evaluation using Silhouette Score

• Cluster selection using the Elbow Method

• Principal Component Analysis (PCA)

• Community profiling

• Translating analytical findings into interpretable community segments
