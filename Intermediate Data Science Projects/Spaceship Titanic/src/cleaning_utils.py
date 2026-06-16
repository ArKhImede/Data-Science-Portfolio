import pandas as pd


def handle_numerical_missing_data(series):
    return series.fillna(series.median())


def handle_categorical_missing_data(series):
    return series.fillna(series.mode()[0])
