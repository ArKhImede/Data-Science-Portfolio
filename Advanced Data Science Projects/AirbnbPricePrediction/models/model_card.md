# 🤖 Model Card

This folder contains information about the machine learning models trained for the **AirbnbPricePrediction** project.

## 📌 Why Are The Models Not Included?

The trained Random Forest models were intentionally excluded from this GitHub repository because they are several hundred megabytes in size and would unnecessarily increase the repository size.

### Model Files

| Model | File |
| -------------------------- | ---------------------------- |
| Random Forest (Baseline) | `random_forest_baseline.pkl` |
| Random Forest (Tuned) | `random_forest_tuned.pkl` |

### Model Sizes

| Model | Size |
| -------------------------- | ---------- |
| Random Forest (Baseline) | ~475 MB |
| Random Forest (Tuned) | ~282 MB |

The Random Forest models are relatively large due to the combination of:

- One-hot encoded categorical features

- Hundreds of decision trees

- Large training dataset

- Complex tree structures storing many learned decision rules

The tuned model is noticeably smaller because limiting the maximum tree depth results in more compact decision trees.

---

# 🧠 Training Dataset

The models were trained using an Airbnb listings dataset containing information about properties, hosts, reviews and locations.

**Target Variable:** `log_price`

The target variable represents the natural logarithm of the Airbnb listing price.

---

# 📊 Features Used

### Numerical Features

- Accommodates
- Bathrooms
- Bedrooms
- Beds
- Number of Reviews
- Review Scores Rating
- Host Response Rate
- Latitude
- Longitude
- Host Year
- Host Month
- Host Days
- Days Since Last Review
- Amenities Count
- Description Length
- Description Word Count
- Accommodates per Bedroom
- Beds per Bedroom
- Bathrooms per Bedroom
- Has WiFi
- Has Kitchen
- Has Heating
- Does Host Respond
- Cleaning Fee

### Categorical Features

- Property Type
- Room Type
- Bed Type
- City
- Neighbourhood
- Zipcode
- Cancellation Policy
- Instant Bookable
- Host Identity Verified
- Host Has Profile Picture

---

# ❌ Excluded Features

The following columns were intentionally removed before training:

- ID
- Name
- Thumbnail URL
- Amenities (replaced by engineered features)
- Description (replaced by engineered features)
- Host Since
- First Review
- Last Review

---

# ⚙️ Preprocessing Pipeline

### Numerical Features

- Median Imputation

- Standard Scaling

### Categorical Features

- Most Frequent Imputation

- One-Hot Encoding (`handle_unknown="ignore"`)

### Pipeline Structure

The preprocessing pipeline was implemented using:

- `Pipeline`

- `ColumnTransformer`

- `Scikit-learn`

All preprocessing transformations were fitted exclusively on the training data.

---

# 🤖 Model Configurations

## Baseline Random Forest

```python
RandomForestRegressor(
    random_state=42,
    n_estimators=100,
)
```

## Tuned Random Forest

The model was optimized using `GridSearchCV`.

The search explored:

- Number of trees

- Maximum tree depth

- Minimum samples required for splitting

- Minimum samples required at leaf nodes

The best hyperparameters can be reproduced by running `05_Hyperparameter_Tuning.ipynb`.

---

# 🔒 Train/Test Strategy

The dataset was randomly split into training and testing sets using:

### Training Set

80% of the observations.

### Test Set

20% of the observations.

### Cross Validation

Hyperparameter tuning used:

- `GridSearchCV`

- 3-fold Cross Validation

---

# 📊 Best Model

The best-performing model was the **Tuned Random Forest Regressor**.

### Performance Metrics

| Metric | Score |
| ------------------- | ---------------- |
| Cross Validation R² | ~0.70 |
| Test R² | ~0.71 |
| MAE | ~0.28 |
| RMSE | ~0.39 |

After converting predictions back from the logarithmic scale, the average prediction error is approximately **€50** per listing.

Although the tuned model only slightly improved predictive performance compared to the baseline model, it generalized well while also producing a considerably smaller serialized model.

---

# 🔄 Reproducing The Models

To recreate the trained models locally:

1. Run `01_EDA.ipynb`

2. Run `02_Preprocessing.ipynb`

3. Run `03_Feature_Engineering.ipynb`

4. Run `04_Modeling.ipynb`

5. Run `05_Hyperparameter_Tuning.ipynb`

6. Run `06_Model_Evaluation.ipynb`

The trained `.pkl` files will be generated automatically inside the `models/` directory.

---

# 📁 Repository Notes

The following models are excluded from this repository due to their size:

- `random_forest_baseline.pkl`

- `random_forest_tuned.pkl`

The complete training pipeline is fully reproducible using the notebooks included in this project.
