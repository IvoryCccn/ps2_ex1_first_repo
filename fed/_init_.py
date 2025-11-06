"""
GDP Analysis Package

A package for loading, cleaning, and visualizing GDP data for
multiple countries.
"""

from .data import load_gdp_data, clean_gdp_data, get_data_summary
from .plot_utils import (
    plot_gdp_trends,
    plot_log_gdp_trends,
    plot_growth_rates
)

__version__ = "0.1.0"
__author__ = "IvoryCccn"
__email__ = "nc681@cam.ac.uk"

__all__ = [
    'load_gdp_data',
    'clean_gdp_data',
    'get_data_summary',
    'plot_gdp_trends',
    'plot_log_gdp_trends',
    'plot_growth_rates',
]
