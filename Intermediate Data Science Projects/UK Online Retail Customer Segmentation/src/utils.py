from aquarel import load_theme
import matplotlib.pyplot as plt


def create_theme_and_change_plot_params():
    theme = load_theme("arctic_dark").set_grid(draw=True, alpha=0.1)
    theme.apply()

    plt.rcParams["axes.titleweight"]

    plt.rcParams.update(
        {
            "axes.titlesize": 16,
            "axes.titleweight": "bold",
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "font.family": "DejaVu Sans",
        }
    )
