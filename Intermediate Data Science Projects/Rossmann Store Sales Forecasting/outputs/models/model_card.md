# 🤖 Model Card

This folder contains information about the machine learning models trained for the **Rossmann Store Sales Forecasting** project.

## 📌 Why Are Some Models Not Included?

Some trained model files were intentionally excluded from this GitHub repository because they exceed GitHub's file size recommendations and would significantly increase repository size.

### Model Files

| Model                 | File                         |
| --------------------- | ---------------------------- |
| Dummy Regressor       | `dummy.joblib`               |
| Linear Regression     | `linear_regression.joblib`   |
| Random Forest         | `random_forest.joblib`       |
| Random Forest (Tuned) | `random_forest_tuned.joblib` |
| XGBoost               | `xg_boost.joblib`            |

### Model Sizes

| Model                 | Size       |
| --------------------- | ---------- |
| Dummy Regressor       | ~6 KB      |
| Linear Regression     | ~6 KB      |
| XGBoost | ~9 KB       | ~968 KB    |
| Random Forest         | Several GB |
| Random Forest (Tuned) | Several GB |

The Random Forest models are particularly large due to the combination of:

* One-hot encoded categorical features

* Hundreds of decision trees

* Large training datasets

* Deep tree structures with many learned splits

## 🧠 Training Dataset

The models were trained using the historical Rossmann daily sales dataset containing:

* Store information

* Daily sales records

* Promotions

* Competition information

**Target Variable**: `Sales`

### Features Used

#### Numerical Features

* Store

* Customers

* Day

* WeekOfYear

* Quarter

* Open

* Promo

* SchoolHoliday

* CompetitionDistance

* CompetitionAgeMonths

* WasPromo2Active

* Year

* Month

* DayOfWeek

#### Categorical Features

* Season

* StoreType

* StateHoliday

* Assortment

* PromoInterval

### Excluded Features

The following columns were excluded from modeling:

* Date

* Competition opening month

* Competition opening year

* Promo2 start week

* Promo2 start year

* Intermediate variables used during feature engineering

## ⚙️ Preprocessing Pipeline

### Numerical Features

* `StandardScaler`

### Categorical Features

* `OneHotEncoder (handle_unknown="ignore")`

### Pipeline Structure

The preprocessing pipeline was implemented using:

* `ColumnTransformer`

* `Pipeline`

* `Scikit-learn`

All preprocessing steps were fitted exclusively on the training data.

## 🤖 Model Configurations

### Dummy Regressor

```python
DummyRegressor(
    strategy="median"
)
```

### Linear Regression

```python
LinearRegression(
    n_jobs=-1
)
```

### Random Forest

```python
RandomForestRegressor(
    n_estimators=200, 
    random_state=42, 
    n_jobs=-1
)
```

### Tuned Random Forest

```python
RandomForestRegressor(
    n_estimators=300, 
    max_depth=None, 
    min_samples_leaf=1, 
    min_samples_split=2, 
    random_state=42, 
    n_jobs=-1
)
```

### XG Boost

```python
XGBRegressor(
    n_estimators=200, 
    random_state=42, 
    n_jobs=-1, 
    objective="reg:squarederror", 
    eval_metric="rmse"
)
```

## 🔒 Train/Validation Strategy

Because this is a time-dependent forecasting problem, random train/test splitting was avoided to prevent temporal leakage. The data was split chronologically:

### Training Set

* All observations from 2013

* All observations from 2014

* January to May 2015

### Validation Set

* June and July 2015

### Cross Validation

Model selection and hyperparameter tuning used `TimeSeriesSplit(n_splits=5)`.

## 📊 Best Model

The best-performing model was the **Tuned Random Forest Regressor**.

### Performance Metrics

| Metric              | Score                      |
| ------------------- | -------------------------- |
| Cross Validation R² | ~0.979                     |
| Test R²             | ~0.98                      |
| MAE                 | ~0.334                     |
| MSE                 | See `final_metrics_df.csv` |
| MAPE                | See `final_metrics_df.csv` |

The tuned Random Forest slightly outperformed the default Random Forest configuration, although the improvement was relatively small. Both tree-based ensemble methods substantially outperformed the linear baseline.

## 🔄 Reproducing The Models

To recreate the models locally:

1. Run cleaning.ipynb

2. Run feature_engineering.ipynb

3. Run EDA.ipynb

4. Run train.ipynb

5. Run tune_best_model.ipynb

6. Run evaluate.ipynb

The trained `.joblib` files will be generated automatically inside the `outputs/models/` directory.

## 📁 Repository Notes

The following models are included in the repository:

* `dummy.joblib`

* `linear_regression.joblib`

* `xg_boost.joblib`

The following models are excluded due to their large size:

* `random_forest.joblib`

* `random_forest_tuned.joblib`