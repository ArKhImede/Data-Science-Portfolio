import pandas as pd
import numpy as np


def extract_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new features from date columns.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with new date features.
    """
    df = df.copy()

    today = pd.to_datetime("2026-07-06")

    df["host_year"] = df["host_since"].dt.year
    df["host_month"] = df["host_since"].dt.month
    df["host_days"] = (today - df["host_since"]).dt.days
    df["days_since_last_review"] = (today - df["last_review"]).dt.days

    df.drop(columns=["host_since", "first_review", "last_review"], inplace=True)

    return df


def create_amenity_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    Count amenities for each listing.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with amenities count.
    """
    df = df.copy()

    df["amenities_count"] = df["amenities"].str.split(",").apply(lambda x: len(x))

    return df


def create_amenity_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create binary features from amenities column.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with different binary features related to listing amenities. Since amenities is summarized, the resulting DataFrame won't contain it.
    """
    df = df.copy()

    df["has_wifi"] = (
        df["amenities"].str.contains("Wireless Internet", na=False).astype("int8")
    )
    df["has_kitchen"] = df["amenities"].str.contains("Kitchen", na=False).astype("int8")
    df["has_heating"] = df["amenities"].str.contains("Heating", na=False).astype("int8")

    df.drop(columns="amenities", inplace=True)

    return df


def create_description_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create features from the listing description.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with new description-related features.
    """
    df = df.copy()

    df["description_length"] = df["description"].apply(len)
    df["description_word_count"] = (
        df["description"].str.split(" ").apply(lambda x: len(x))
    )

    df.drop(columns="description", inplace=True)

    return df


def create_host_response_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create binary column indicating whether a host has a recorded response rate.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with new binary column added to the DataFrame.
    """
    df = df.copy()

    df["does_host_respond"] = (df["host_response_rate"].notna()).astype("int8")

    return df


def create_occupancy_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create occupancy-related ratios.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with new ratio features using occupancy-related columns.
    """
    df = df.copy()

    df["accommodates_per_bedroom"] = np.where(
        df["bedrooms"] != 0, df["accommodates"] / df["bedrooms"], 0
    )
    df["beds_per_bedroom"] = np.where(
        df["bedrooms"] != 0, df["beds"] / df["bedrooms"], 0
    )
    df["bathrooms_per_bedroom"] = np.where(
        df["bedrooms"] != 0, df["bathrooms"] / df["bedrooms"], 0
    )

    return df


def group_property_types(df: pd.DataFrame, threshold: float = 0.01) -> pd.DataFrame:
    """
    Group rare property types into 'Other'.

    Parameters
    ----------
    df: pd.DataFrame
       Airbnb listings dataset.

    Returns
    -------
    pd.DataFrame
       DataFrame with rare property types grouped into 'Other' feature.
    """
    df = df.copy()

    property_counts = df["property_type"].value_counts().reset_index()
    rare = property_counts[property_counts["count"] < (df.shape[0] * threshold)][
        "property_type"
    ].to_list()

    df["property_type"] = np.where(
        df["property_type"].isin(rare), "Other", df["property_type"]
    )

    return df
