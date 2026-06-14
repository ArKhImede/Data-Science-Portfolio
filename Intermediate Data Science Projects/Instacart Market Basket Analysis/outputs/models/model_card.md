# 🤖 Model Card

This folder contains information about the machine learning models trained for the **Instacart Market Basket Analysis** project.

## 📌 Why Are The Models Not Included?

The trained model files were intentionally excluded from this GitHub repository because one of them exceeds GitHub's file size limits and would significantly increase repository size.

### Model Files

| Model               | File                         |
| ------------------- | ---------------------------- |
| Logistic Regression | `logistic_regression.joblib` |
| Random Forest       | `random_forest.joblib`       |
| XGBoost             | `xgboost.joblib`             |

### Model Sizes

| Model               | Size     |
| ------------------- | -------- |
| Logistic Regression | ~9 KB    |
| Random Forest       | ~3.75 GB |
| XGBoost             | ~402 KB  |

The Random Forest model is particularly large due to the combination of:

* One-hot encoded categorical features

* High-cardinality product categories

* 100 decision trees

* Large training dataset

## 🧠 Training Dataset

The models were trained using a sample of **1,000,000 purchase events** extracted from the Instacart dataset.

### Target Variable

`reordered`

* 1 = Product reordered
* 0 = Product not reordered

### Features Used

#### Numerical Features

* order_number

* days_since_prior_order

* add_to_cart_order

* product_name_length

#### Categorical Features

* aisle

* department

* part_of_day_purchase

### Excluded Features

The following columns were removed to avoid data leakage or unnecessary model complexity:

* order_id

* user_id

* product_id

* product_name

* eval_set

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

### Logistic Regression

```python
LogisticRegression(
    max_iter=1000,
    class_weight="balanced",
    random_state=42
)
```

### Random Forest

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)
```

### XGBoost

```python
XGBClassifier()
```

## 🔒 Train/Test Strategy

To better simulate real-world predictions and avoid user leakage:

* Users were split before creating training and testing datasets.

* Users appearing in the training set never appeared in the test set.

* Approximately 80% of users were used for training.

* Approximately 20% of users were used for testing.

This approach provides a more realistic estimate of model performance on unseen customers.

## 📊 Best Model

The best-performing model was **XGBoost**.

### Performance Metrics

| Metric    | Score |
| --------- | ----- |
| Accuracy  | ~0.74 |
| Precision | ~0.73 |
| Recall    | ~0.86 |
| ROC AUC   | ~0.80 |

XGBoost achieved the strongest balance between identifying reorder events and minimizing classification errors.

## 🔄 Reproducing The Models

To recreate the models locally:

1. Run `cleaning.ipynb`
2. Run `feature_engineering.ipynb`
3. Run `train.ipynb`

The trained `.joblib` files will be generated automatically inside the `outputs/models/` directory.
