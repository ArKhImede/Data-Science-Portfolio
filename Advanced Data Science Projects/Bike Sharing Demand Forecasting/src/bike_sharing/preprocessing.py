import pandas as pd


def convert_date_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert date column from string to datetime format.

    Parameters
    ----------
    df: pd.DataFrame
       Bike Sharing dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame with converted date column.
    """
    df = df.copy()

    df["dteday"] = pd.to_datetime(df["dteday"], errors="coerce")

    return df


def remove_leakage_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove columns that leak data.

    Parameters
    ----------
    df: pd.DataFrame
       Bike Sharing dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame with leakage features removed.
    """
    df = df.copy()
    leakage_columns = ["casual", "registered"]
    df.drop(columns=leakage_columns, inplace=True)

    return df


def sort_by_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort the DataFrame by date and hour.

    Parameters
    ----------
    df: pd.DataFrame
       Bike Sharing dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame sorted by date and hour.
    """
    df = df.copy()

    return df.sort_values(by=["dteday", "hr"], ascending=True).reset_index(drop=True)


def drop_irrelevant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop columns not useful for machine learning.

    Parameters
    ----------
    df: pd.DataFrame
       Bike Sharing dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame without useless columns.
    """
    df = df.copy()

    useless_columns = ["instant"]

    return df.drop(columns=useless_columns)
