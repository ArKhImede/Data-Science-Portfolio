from sklearn.pipeline import Pipeline
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

from bike_sharing.modeling import create_xgb_model


def create_objective(preprocessor, X_train, y_train):
    """
    Create Optuna objective function for XGBoost optimization.
    """

    tscv = TimeSeriesSplit(n_splits=5)

    def objective(trial):

        params = {
            "n_estimators": trial.suggest_int("n_estimators", 100, 500),
            "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.2),
            "max_depth": trial.suggest_int("max_depth", 3, 10),
            "subsample": trial.suggest_float("subsample", 0.5, 1.0),
            "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
        }

        model = create_xgb_model(params)

        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )

        scores = cross_val_score(pipeline, X_train, y_train, cv=tscv, scoring="r2")

        return scores.mean()

    return objective
