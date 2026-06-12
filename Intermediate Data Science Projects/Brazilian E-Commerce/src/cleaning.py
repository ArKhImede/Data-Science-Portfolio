import pandas as pd

def convert_to_datetime(feature: pd.Series) -> pd.Series:
    return pd.to_datetime(feature, errors="coerce", format="%Y-%m-%d %H:%M:%S")

def replace_and_make_title_case(feature: pd.Series) -> pd.Series:
    return feature.str.replace("_", " ", regex=False).str.title()