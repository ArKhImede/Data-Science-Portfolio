import pandas as pd
import numpy as np


def create_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create date-related features.

    Parameters
    ----------
    df: pd.DataFrame
       Bike Sharing dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame with new date-related features added.
    """
    df = df.copy()

    df["year"] = df["dteday"].dt.year
    df["day"] = df["dteday"].dt.day

    return df


def create_cyclical_encodings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create cyclical encodings.

    Parameters
    ----------
    df: pd.DataFrame
       Bike Sharing dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame with cyclical encodings added.
    """
    df = df.copy()

    df["hour_sin"] = np.sin(2 * np.pi * df["hr"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hr"] / 24)
    df["month_sin"] = np.sin(2 * np.pi * df["mnth"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["mnth"] / 12)

    return df


def engineer_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create lag features.

    Parameters
    ----------
    df: pd.DataFrame
       Bike Sharing dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame with new lag features.
    """
    df = df.copy()

    df["cnt_lag_1"] = df["cnt"].shift(periods=1)
    df["cnt_lag_24"] = df["cnt"].shift(periods=24)
    df["cnt_lag_168"] = df["cnt"].shift(periods=168)

    return df
