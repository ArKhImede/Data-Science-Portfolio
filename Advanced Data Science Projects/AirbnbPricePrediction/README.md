# 🏠 Airbnb Price Prediction

Exploratory Data Analysis (EDA), Feature Engineering and Machine Learning project using an Airbnb listings dataset. This project analyzes property characteristics, host information, amenities and geographical features to understand the factors influencing listing prices and build predictive models for Airbnb price estimation.

## 📌 Project Overview

The purpose of this project is to analyze Airbnb listings and uncover insights about:

- 💰 Listing prices

- 🏠 Property characteristics

- 🛏️ Room types

- 📍 Location effects

- ⭐ Reviews and ratings

- 👤 Host information

- 🛠️ Property amenities

- 🤖 Machine learning models for price prediction

This project focuses on:

- Data cleaning

- Data preprocessing

- Feature engineering

- Exploratory Data Analysis (EDA)

- Data visualization

- Correlation analysis

- Machine Learning

- Pipeline construction

- Hyperparameter tuning

- Model evaluation

## 📂 Dataset

The dataset contains Airbnb listings from multiple cities together with property, host and review information.

The dataset includes features such as:

- Listing information

- Property characteristics

- Room type

- Amenities

- Host information

- Review statistics

- Geographic coordinates

- Price (log-transformed)

You can use this [link](https://www.kaggle.com/datasets/rupindersinghrana/airbnb-price-dataset) to download the dataset.

## 🛠️ Technologies Used

• ```🐍 Python```

• ```🐼 Pandas```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```📈 NumPy```

• ```📉 SciPy```

• ```🌲 Scikit-learn```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

## 🧹 Data Cleaning

Several preprocessing steps were performed to improve data quality before feature engineering.

### 📅 Date Conversion

Converted date columns into datetime format:

- Host since

- First review

- Last review

### 📊 Percentage Conversion

Converted:

- Host response rate

from percentage strings into numerical values.

### ✅ Boolean Conversion

Converted boolean variables into integer format to simplify modeling.

### 🗑️ Feature Removal

Removed non-informative features including:

- Listing ID

- Thumbnail URL

- Listing name

### 🧩 Missing Value Handling

#### Numerical Features

Missing values were replaced using the median for:

- Bathrooms

- Bedrooms

- Beds

- Review scores

#### Categorical Features

Missing values were replaced with "Unknown" for:

- Neighbourhood

- Zipcode

- Host verification

- Host profile picture

## ⚙️ Feature Engineering

Several new features were created to improve predictive performance.

### 📅 Date Features

Extracted:

- Host year

- Host month

- Days since host joined Airbnb

- Days since last review

### 🛠️ Amenities Features

Created:

- Amenities count

- Has WiFi

- Has kitchen

- Has heating

### 📝 Description Features

Generated:

- Description length

- Description word count

### 👤 Host Features

Created:

Does host respond

which indicates whether a response rate exists.

### 🏠 Occupancy Ratios

Engineered:

- Accommodates per bedroom

- Beds per bedroom

- Bathrooms per bedroom

### 🏡 Property Type Grouping

Rare property types were grouped into an Other category to reduce high-cardinality categorical variables.

## 📊 Exploratory Data Analysis

### 📈 Dataset Overview

Explored:

- Dataset dimensions

- Data types

- Summary statistics

- Duplicate records

- Missing values

### 💰 Target Variable Analysis

Investigated:

- Log price distribution

- Price variability

### 📊 Numerical Feature Analysis

Examined:

- Feature distributions

- Boxplots

- Skewness

- Outliers

### 🏠 Categorical Feature Analysis

Analyzed:

- Room types

- Cities

- Property types

- Cancellation policies

### 🔗 Correlation Analysis

Explored relationships between numerical variables and listing price using a correlation matrix.

### 📉 Feature Relationships

Compared listing prices across:

- Room types

- Cities

- Property types

- Cancellation policies

## 🤖 Machine Learning

The objective was to predict Airbnb listing prices.

### 📉 Dummy Regressor

Baseline model using the median price.

### 📈 Linear Regression

Linear benchmark model.

### 🌲 Random Forest Regression

Tree-based ensemble model used as the primary predictive model.

### 🌿 Gradient Boosting Regression

Boosting model included for comparison.

### 🔧 Preprocessing Pipeline

A reusable Scikit-learn pipeline was built using:

- Numerical Features

- Median imputation

- Standard scaling

- Categorical Features

- Most frequent imputation

- One-hot encoding

The preprocessing and model were combined into a single reusable pipeline.

## ⚙️ Hyperparameter Tuning

Random Forest was optimized using GridSearchCV.

The search explored:

- Number of trees

- Maximum depth

- Minimum samples split

- Minimum samples leaf

### 📏 Evaluation Metrics

Models were evaluated using:

- R² Score

- Mean Absolute Error (MAE)

- Root Mean Squared Error (RMSE)

## 🔍 Key Insights

### 🏠 Entire homes command the highest prices

Entire homes/apartments consistently have higher prices than private or shared rooms.

### 📍 Location strongly influences price

Latitude and longitude are among the most important predictive variables, indicating that geographical location heavily affects Airbnb pricing.

### 🛏️ Larger properties are more expensive

Bathrooms, bedrooms, beds and accommodation capacity all show positive relationships with listing price.

### ⭐ Review activity provides useful information

Listings with more recent reviews contain predictive information, although its impact is smaller than location and room type.

### 🛠️ Engineered amenities add modest predictive value

Amenity-related features improve the dataset but contribute less than structural property characteristics.

## 🤖 Machine Learning Results

### 📉 Dummy Regressor

Performed poorly, providing a simple baseline for comparison.

### 📈 Linear Regression

Captured linear relationships but underperformed compared to ensemble methods.

### 🌲 Random Forest

Produced the best overall predictive performance among the evaluated models.

The tuned model achieved approximately:

- Test R²: 0.71

- MAE: 0.28 (log-price)

- RMSE: 0.39

Average prediction error corresponds to roughly €50 after converting predictions back from the logarithmic scale.

### 🌿 Gradient Boosting

Improved over Linear Regression but did not outperform Random Forest.

### ⚙️ Hyperparameter Tuning

GridSearchCV improved the Random Forest model while maintaining good generalization between cross-validation and test performance.

## 📈 Model Evaluation

The final model was evaluated using several diagnostic techniques.

Performed:

- Actual vs Predicted analysis

- Residual distribution analysis

- Residual scatter plots

- Feature importance analysis

- Error analysis by city

- Error analysis by property type

The evaluation showed moderate overfitting, with prediction uncertainty increasing for high-priced listings.

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies
```
pip install pandas numpy matplotlib seaborn scipy scikit-learn joblib pyarrow
```

### 3️⃣ Run Jupyter Notebook
```
jupyter notebook
```

Run the notebooks in the following order:

- 01_EDA.ipynb

- 02_Preprocessing.ipynb

- 03_Feature_Engineering.ipynb

- 04_Modeling.ipynb

- 05_Hyperparameter_Tuning.ipynb

- 06_Model_Evaluation.ipynb

## 📚 What I Learned

Through this project I practiced:

- Working with real-world Airbnb datasets

- Building reusable preprocessing functions

- Creating feature engineering pipelines

- Handling missing values and data type conversions

- Working with datetime features

- Engineering categorical and numerical features

- Exploratory Data Analysis (EDA)

- Correlation analysis

- Building Scikit-learn preprocessing pipelines

- Comparing multiple regression models

- Hyperparameter tuning using GridSearchCV

- Evaluating regression models with diagnostic plots

- Interpreting feature importance

- Saving complete machine learning pipelines using Joblib

- Building a reproducible end-to-end machine learning workflow
