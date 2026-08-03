import pandas as pd


def convert_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert date columns from strings to datetime format.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame with converted date columns.
    """
    df = df.copy()
    date_columns: list[str] = ["host_since", "first_review", "last_review"]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    return df


def convert_response_rate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert host_response_rate feature from str to integer.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with host_response_rate column converted.
    """
    df = df.copy()

    df["host_response_rate"] = pd.to_numeric(
        df["host_response_rate"].str.replace("%", ""), errors="coerce"
    )

    return df


def convert_boolean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert boolean columns to integer.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with boolean columns converted.
    """
    df = df.copy()
    boolean_cols: list[str] = ["cleaning_fee"]

    for col in boolean_cols:
        df[col] = df[col].astype("int8")

    return df


def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop non-useful columns.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with unused features dropped.
    """
    df = df.copy()
    unused_columns: list[str] = ["id", "thumbnail_url", "name"]

    df.drop(columns=unused_columns, inplace=True)

    return df


def handle_numeric_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle numeric missing values.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame without numeric missing values.
    """
    df = df.copy()
    numeric_columns: list[str] = [
        "bathrooms",
        "bedrooms",
        "beds",
        "review_scores_rating",
    ]

    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())

    return df


def handle_categorical_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle categorical missing values.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame without categorical missing values.
    """
    df = df.copy()

    categorical_columns: list[str] = [
        "host_has_profile_pic",
        "host_identity_verified",
        "neighbourhood",
        "zipcode",
    ]

    for col in categorical_columns:
        df[col] = df[col].fillna("Unknown")

    return df
