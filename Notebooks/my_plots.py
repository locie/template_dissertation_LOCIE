# de Sarah Juricic LOCIE USMB
# on met dans my_plots toutes les fonctions trop lourdes
# et les paramètres de définition des plots, pour alléger le notebook


import numpy as np
import pandas as pd
import scipy

def set_size(width, fraction=1, subplot=[1, 1], shrink_height=1.):
    """ Set aesthetic figure dimensions to avoid scaling in latex.

    Parameters
    ----------
    width: float
            Width in pts
    fraction: float
            Fraction of the width which you wish the figure to occupy
    shrink_height: float
            fraction of the height to crop figure in height

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * shrink_height * (subplot[0] / subplot[1])

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim


def get_custom_colors():
    return ['#E69F00',
          '#56B4E9',
          '#009E73',
          '#F0E442',
          '#0072B2',
          '#D55E00',
          '#CC79A7']


