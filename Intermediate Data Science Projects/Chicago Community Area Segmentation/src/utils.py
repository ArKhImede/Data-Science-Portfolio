import matplotlib.pyplot as plt
import matplotlib as mpl
import catppuccin


def apply_theme_and_set_plot_params():

    mpl.style.use("mocha")

    plt.rcParams.update(
        {
            "axes.titlesize": 16,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "axes.labelsize": 14,
            "font.family": "monospace",
        }
    )
