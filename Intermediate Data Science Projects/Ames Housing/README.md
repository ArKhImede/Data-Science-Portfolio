# 🏠 Ames Housing Price Prediction 

Exploratory Data Analysis (EDA), Feature Engineering, Statistical Analysis, and Machine Learning project using the Ames Housing dataset. This project explores housing characteristics, sale price drivers, neighborhood effects, and predictive modeling techniques to estimate house sale prices. 

## 📌 Project Overview 

The purpose of this project is to analyze residential housing data and uncover insights about: 

• 💰 House sale prices 

• 🏡 Property characteristics 

• 📏 Living area and house quality 

• 🏘️ Neighborhood influence 

• 🏗️ House age and remodeling effects 

• 📊 Statistical differences across sale conditions 

• 🤖 Machine learning regression models 

• 🎯 Housing price prediction This project focuses on: 

• Data cleaning 

• Missing value handling 

• Feature engineering 

• Exploratory Data Analysis (EDA) 

• Statistical hypothesis testing 

• Machine Learning 

• Model comparison 

•Pipeline construction 

## 📂 Dataset 

The dataset contains detailed information about residential properties sold in Ames, Iowa, including: 

• Sale price 

• House quality and condition 

• Living area 

• Lot size 

• Neighborhood 

• Foundation type 

• Year built 

• Year remodeled 

• Garage information 

• Basement information 

• Porch and deck features 

• Utility and zoning information 

The Ames Housing dataset is widely used as a practical alternative to the Boston Housing dataset for regression and machine learning projects. 

To note, I completed the project a few years ago and I don't remember the correct Kaggle link from which I downloaded the dataset. The closest dataset I have found that looks similar to mine is [this](https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset) one.

## 🛠️ Technologies Used 

• ```🐍 Python```

• ```🐼 Pandas```

• ```🔢 NumPy```

• ```📊 Matplotlib```

• ```🎨 Seaborn```

• ```📈 SciPy```

• ```🤖 Scikit-learn```

• ```💾 Joblib```

• ```📓 Jupyter Notebook```

• ```🎨 Aquarel```

• ```⚡ XGBoost```


## 🧹 Data Cleaning 

Before analysis, several preprocessing steps were performed: 

• Removed extreme outliers from Gross Living Area 

•Handled missing values using domain-specific strategies 

• Replaced missing categorical values representing absent features with "None" 

• Filled Lot Frontage values using neighborhood medians 

• Filled missing numerical values using column medians 

• Filled remaining categorical values using mode 

• Converted object columns into categorical data types 

• Saved a cleaned dataset for downstream analysis 

## ⚙️ Feature Engineering 

Several new features were created to improve interpretability and predictive performance: 

### 🏡 Property Age Features 

• House Age 

• Remod Age 

• Was Remodelled 

### 🚿 Housing Utility Features 

• Total Bathrooms 

• Total Porch SF 

### 📐 Interaction Features 

• Overall Qual × Gross Living Area 

• Total Rooms × Gross Living Area 

### 📅 Temporal Features • Built Decade 

### 🔥 Property Amenities 

• Has Pool 

• Has Fireplace 

These engineered features were added to the final modeling dataset. 

## 📊 Exploratory Data Analysis 

### 💰 Sale Price Analysis 

• Examined sale price distribution 

• Measured skewness 

• Compared mean and median values 

### 📏 Gross Living Area Analysis 

• Investigated distribution shape 

• Evaluated kurtosis 

• Identified unusually large homes 

### 🏗️ House Age & Remodeling Trends 

• Compared construction and remodeling years 

• Investigated housing stock age 

### 🏡 Quality & Condition Analysis 

• Explored distributions of: 

  o Overall Quality 
  
  o Overall Condition 

### 💵 Sale Price Relationships 

• Compared house quality versus sale price 

• Investigated year built versus sale price 

### 📈 Correlation Analysis 

• Identified the strongest numerical predictors of sale price 

• Evaluated the usefulness of engineered features 

### 📊 ANOVA & Tukey HSD 

• Tested whether sale price means differed across sale conditions 

• Identified which sale condition groups significantly differed 

### 🏘️ Group Analysis Compared sale prices across: 

• Street types 

• Foundation types 

• Neighborhoods 

## 🤖 Machine Learning 

Four regression models were trained to predict house sale prices: 

### 📉 Dummy Regressor 

Baseline model using the mean sale price. 

### 🎯 Support Vector Regression (SVR) 

Support Vector Machine model for regression tasks. 

### 🌲 Random Forest Regressor 

Ensemble tree-based model using multiple decision trees. 

### ⚡ XGBoost Regressor 

Gradient boosting model designed for high predictive performance. 

### 🔧 Model Pipeline 

A reusable preprocessing pipeline was built using: 

• ```StandardScaler``` for numerical features 

• ```OneHotEncoder(handle_unknown="ignore")``` for categorical features 

• ```ColumnTransformer``` for automated preprocessing 

The preprocessing pipeline was integrated directly into each machine learning model to ensure consistent transformations during training and inference. 

### 📏 Evaluation Metrics 

Models were evaluated using: 

• Cross-Validation R² 

• Test R² 

• Mean Absolute Error (MAE) 

• Mean Squared Error (MSE) 

• Mean Absolute Percentage Error (MAPE) 

## 🔍 Key Insights

### 💰 House prices are positively skewed 

Most homes sell between approximately $100k and $250k, while a smaller number of luxury properties create a long right tail. 

### 📏 Larger homes generally sell for more 

Gross Living Area is one of the strongest predictors of sale price and shows a strong positive relationship with property value. 

### 🏡 House quality strongly impacts price 

Higher Overall Quality ratings are consistently associated with higher sale prices. 

### 🏗️ Newer homes tend to command higher prices 

More recently built properties generally sell for more than older homes.

### 📈 Several features strongly correlate with sale price 

The strongest correlations include: 

• Overall Quality (~0.8) 

• Total Basement Area (~0.7) 

• Gross Living Area (~0.7) 

### 📊 Sale condition affects pricing 

ANOVA results showed statistically significant differences in average sale prices across sale conditions. 

### 🛣️ Paved streets are associated with higher prices 

Properties located on paved streets exhibit substantially higher average sale prices than those on gravel roads. 

### 🏘️ Neighborhood is a major price driver 

Median sale prices vary dramatically across neighborhoods, ranging from approximately $88k to over $300k. 

## 🤖 Machine Learning Results 

### 📉 Dummy Regressor 

Served as a baseline model by always predicting the average sale price. 

### 🎯 Support Vector Regression (SVR) 

SVR struggled to learn the relationship between predictors and target values. 

Key observations: 

• Negative R² score 

• Performed worse than the baseline model 

• Failed to capture nonlinear housing patterns effectively 

### 🌲 Random Forest Regressor 

Random Forest achieved: 

• Test R² ≈ 0.93 

• MAE ≈ $13.8k 

• MAPE ≈ 8% 

The model successfully captured complex nonlinear relationships between housing characteristics and sale price. 

### ⚡ XGBoost Regressor 

XGBoost achieved: 

• Test R² ≈ 0.93 

• MAE ≈ $13.8k 

• MAPE ≈ 8% 

XGBoost produced slightly better results than Random Forest, although both models performed nearly identically. 

### 🏆 Best Models 

The strongest models were: 

• Random Forest 

• XGBoost 

Both substantially outperformed the baseline and SVR models. The results suggest that housing prices are driven by highly nonlinear relationships that are best captured by tree-based ensemble methods. 

## 🚀 How to Run the Project 

### 1️⃣ Clone the repository

```
git clone https://github.com/ArKhImede/Data-Science-Portfolio.git
```

### 2️⃣ Install dependencies

```
pip install pandas numpy matplotlib seaborn scipy scikit-learn xgboost joblib pyarrow aquarel
```

### 3️⃣ Run Jupyter Notebook

```
jupyter notebook
```

Run the notebooks in the following order: 

1. cleaning.ipynb

2. feature_engineering.ipynb

3. EDA.ipynb

4. train.ipynb

5. evaluate.ipynb

## 📚 What I Learned Through this project I practiced: 

• Advanced missing value handling 

• Feature engineering techniques 

• Working with high-dimensional tabular data 

• Exploratory Data Analysis (EDA) 

• Statistical hypothesis testing using ANOVA 

• Tukey HSD post-hoc analysis 

• Building preprocessing pipelines 

• Handling mixed numerical and categorical data 

• Model comparison and benchmarking 

• Cross-validation 

• Ensemble learning methods 

• Regression model evaluation 

• Model persistence using Joblib 

• Extracting business insights from real-world housing data
