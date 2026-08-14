# 🐧 Palmer Penguins

Exploratory Data Analysis (EDA), statistical analysis, and Machine Learning project using the Palmer Penguins dataset. This project explores penguin species characteristics, body mass distributions, flipper measurements, dietary differences, and predictive machine learning models using Python.

## 📌 Project Overview

The purpose of this project is to analyze penguin biological measurements and uncover insights about:

• 🐧 Penguin species differences

• 📏 Flipper length distributions

• ⚖️ Body mass comparisons

• 🍽️ Dietary impact on body mass

• 🧬 Statistical differences across groups

• 📊 Correlations between physical traits

• 🤖 Machine learning classification models

• 📉 Regression analysis for body mass prediction

This project focuses on:

• Data cleaning

• Data preprocessing

• Exploratory Data Analysis (EDA)

• Statistical hypothesis testing

• Machine Learning

• Data visualization

• Animated visualizations

## 📂 Dataset

The dataset contains biological and ecological measurements for multiple penguin species, including:

• Species

• Island

• Bill length

• Bill depth

• Flipper length

• Body mass

• Sex

• Diet

• Life stage

• Year

The dataset includes observations for:

• Adelie penguins

• Chinstrap penguins

• Gentoo penguins

The dataset used in this project is based on the Palmer Penguins dataset.

To note, I completed the project a few years ago and I don't remember the correct Kaggle link from which I downloaded the dataset. The closest dataset I have found that looks similar to mine is [this](https://www.kaggle.com/datasets/samybaladram/palmers-penguin-dataset-extended?select=palmerpenguins_extended.csv) one.

## 🛠️ Technologies Used

•	```🐍 Python```

•	```🐼 Pandas```

•	```📊 Matplotlib```

•	```📓 Jupyter Notebook```

• ```🔢 NumPy```

• ```🤖 Scikit-learn```

• ```🎨 Seaborn```

• ```📈 SciPy```

• ```📈 Statsmodels```

## 🧹 Data Cleaning

Before analysis, several preprocessing steps were performed:

• Renamed columns for readability

• Converted categorical columns into category data types

• Standardized categorical text capitalization

• Checked and handled missing values

• Optimized dataframe memory usage

• Created summary statistics tables

## 📊 Exploratory Data Analysis

### 📏 Flipper Length Distribution by Species and Sex

• Compared flipper length distributions across:

  o Species
  
  o Sex

• Visualized mean flipper lengths using histograms

### ⚖️ Average Body Mass Analysis

• Compared average body mass across:

  o Species
  
  o Sex

• Identified major differences between penguin groups

### 📈 Species Body Mass Metrics

• Compared:

  o Mean body mass
  
  o Minimum body mass
  
  o Maximum body mass

across penguin species.

### 🐣 Juveniles vs Adults Comparison

• Compared average body mass between:

  o Juveniles
  
  o Adults

across multiple years.

### 🎞️ Animated Bill Depth Visualization

• Created an animated line plot showing bill depth distributions across diet types:

  o Fish
  
  o Krill
  
  o Parental
  
  o Squid

### 🏝️ Pivot Table Analysis

• Built pivot tables comparing mean flipper lengths by:

  o Island
  
  o Species

### 📊 Statistical Analysis (ANOVA)

• Performed one-way ANOVA to test whether body mass differs significantly across diet groups.

### 🔬 Tukey’s Honest Significant Difference (HSD)

• Identified which diet groups differed significantly in terms of body mass.

## 🤖 Machine Learning

### 🧠 Support Vector Machine (SVM) Classification

An SVM classifier was trained to predict penguin species using:

• Bill length

• Bill depth

• Flipper length

• Body mass

• Sex

• Diet

Model evaluation metrics included:

• Accuracy score

• Precision

• Recall

• F1-score

• Confusion matrix

### 📉 Linear Regression

A Linear Regression model was trained to predict penguin body mass using:

• Flipper length

Model evaluation metrics included:

• R² Score

• Mean Squared Error (MSE)

• Mean Absolute Error (MAE)

• Root Mean Squared Error (RMSE)

• Mean Absolute Percentage Error (MAPE)

• Residual analysis

## 🔍 Key Insights

### 📏 Gentoo penguins generally have the largest flipper lengths

Male and female Gentoo penguins displayed higher average flipper lengths than Adelie and Chinstrap penguins.

### ⚖️ Gentoo penguins are the heaviest species

Average body mass was highest among Gentoo penguins, followed by Chinstrap and Adelie penguins.

### 📈 Body mass remained relatively stable over time

From 2021 to 2025, average body mass showed only minor fluctuations across life stages.

### 🍽️ Diet strongly affects body mass

ANOVA results showed statistically significant differences in body mass across diet categories.

### 🔬 All diet groups differ significantly

Tukey’s HSD test confirmed significant mean body mass differences between all diet groups.

### 📊 Flipper length and body mass are strongly correlated

Penguins with larger flipper lengths generally tended to have greater body mass.

## 🤖 Machine Learning Results

### 🧠 SVM Classification Performance

The SVM model achieved:

• Accuracy Score: ~57%

Key observations:

• Better performance for Adelie and Gentoo penguins

• Lower precision for Chinstrap penguins due to class imbalance

• Recall remained relatively balanced across species

### 📉 Linear Regression Performance

The Linear Regression model achieved:

• R² Score: ~0.65

• MAE: ~604g

• MAPE: ~13%

The model explains approximately 65% of the variance in penguin body mass using flipper length alone.

Residual analysis suggests that although the model captures the overall trend, prediction errors remain substantial for some observations.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas matplotlib numpy scikit-learn seaborn scipy statsmodels
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

## 📚 What I Learned

Through this project I practiced:

• Data cleaning and preprocessing

• Working with categorical data

• Statistical hypothesis testing

• ANOVA and Tukey HSD analysis

• Exploratory Data Analysis (EDA)

• Advanced data visualization

• Animated visualizations with Matplotlib

• Building machine learning classification models

• Regression modeling

• Model evaluation using classification and regression metrics

• Interpreting residual plots

• Extracting insights from biological datasets
