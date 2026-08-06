from xgboost import XGBRegressor


def create_xgb_model(
    params: dict | None = None, random_state: int = 42, n_jobs: int = -1
) -> XGBRegressor:
    """
    Create XG Boost model.

    Parameters
    ----------
    params: dict | None
        Additional, user-provided parameters for the model.
    random_state: int
        Number provided for reproducibility.
    n_jobs: int
        How many CPU-based tasks to run in parallel.
    Returns
    -------
    XGBRegressor
        The XG Boost regressor model.
    """
    default_params = {"random_state": random_state, "n_jobs": n_jobs}

    if params:
        default_params.update(params)

    return XGBRegressor(**default_params)
