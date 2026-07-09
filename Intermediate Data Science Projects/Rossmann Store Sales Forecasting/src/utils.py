import pandas as pd
import matplotlib.pyplot as plt
import catppuccin


def get_season(date) -> str:
    if not date:
        return "None"

    seasons = ["Spring", "Summer", "Autumn", "Winter"]
    month = date.month

    if month in [3, 4, 5]:
        return seasons[0]
    elif month in [6, 7, 8]:
        return seasons[1]
    elif month in [9, 10, 11]:
        return seasons[2]
    else:
        return seasons[3]


def set_theme_and_plot_params():

    plt.style.use("frappe")
    plt.rcParams.update(
        {
            "axes.titlesize": 18,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "axes.labelsize": 14,
            "font.family": "monospace",
            "axes.titleweight": "bold",
            "figure.dpi": 120,
        }
    )
