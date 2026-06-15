# 🤖 Model Card

This folder contains information about the machine learning models trained for the **OpenAQ Air Quality** project.

## 📌 Why Are The Models Not Included?

The trained model files were intentionally excluded from this GitHub repository because one of them exceeds GitHub's file size limits and would significantly increase repository size.

### Model Files

| Model | File |
|---------|---------|
| Dummy Regressor | `dummy.joblib` |
| Linear Regression | `linear_regression.joblib` |
| SVR | `svr.joblib` |
| Random Forest | `random_forest.joblib` |
| XGBoost | `xg_boost.joblib` |

### Model Sizes

| Model | Size |
|---------|---------|
| Dummy Regressor | ~245 KB |
| Linear Regression | ~343 KB |
| SVR | ~9.4 MB |
| Random Forest | ~320 MB |
| XGBoost | ~419 KB |

The Random Forest model is particularly large due to the combination of:

* One-hot encoded categorical features

* Multiple high-cardinality location variables

* 100 decision trees

* Large training dataset

Because the repository is intended to showcase the complete data science workflow rather than distribute trained artifacts, the models can be reproduced locally using the provided notebooks and source code.

## 🧠 Training Dataset

The models were trained using the feature-engineered OpenAQ dataset.

### Target Variable

`Value`

Represents the recorded pollution concentration level for a given pollutant measurement.

### Features Used

#### Numerical Features

* Val Lag 1 Day

* Year

* Month

* Day

* Month Sin

* Month Cos

* Latitude

* Longitude

* Has Coordinates

* Has City

#### Categorical Features

* Country Code

* Pollutant

* Unit

* Country Label

* City

* Location

* Pollutant Danger

### Excluded Features

The following columns were removed or transformed during feature engineering:

* Last Updated

* Coordinates

## ⚙️ Preprocessing Pipeline

### Numerical Features

* Median Imputation

* StandardScaler

### Categorical Features

* Most Frequent Imputation

* OneHotEncoder (`handle_unknown="ignore"`)

### Pipeline Structure

The preprocessing pipeline was implemented using:

* ColumnTransformer

* Pipeline

* Scikit-learn

All preprocessing steps were fitted exclusively on the training data.

## 🤖 Model Configurations

### Dummy Regressor

```python
DummyRegressor(
    strategy="mean"
)
```

### Linear Regression

```python
LinearRegression()
```

### Support Vector Regression (SVR)

```python
SVR(
    kernel="rbf"
)
```

### Random Forest Regressor

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

### XGBoost Regressor

```python
XGBRegressor(
    n_estimators=100,
    random_state=42
)
```

## 🔒 Train/Test Strategy

The dataset was split using a standard train-test split strategy:

* Approximately 80% of observations were used for training.

* Approximately 20% of observations were used for testing.

* Random state was fixed to 42 to ensure reproducibility.

In addition, 5-fold cross-validation was used during model evaluation to provide more robust performance estimates.

## 📊 Best Model

The best-performing model was **XGBoost Regressor**.

Key observations:

* Lowest Mean Absolute Error (MAE)

* Lowest Mean Squared Error (MSE)

* Strongest overall predictive performance

Feature importance analysis showed that geographic variables were among the most influential predictors of pollution levels.

## 🔄 Reproducing The Models

To recreate the models locally:

1. Run `cleaning.ipynb`

2. Run `feature_engineering.ipynb`

3. Run `train.ipynb`

4. Run `evaluate.ipynb`

The trained `.joblib` files will be generated automatically inside the `outputs/models/` directory.
