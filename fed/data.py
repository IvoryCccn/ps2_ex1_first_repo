"""
Data loading and cleaning functions for GDP analysis.
"""

from typing import Any
import pandas as pd
import numpy as np


def load_gdp_data(path: str) -> pd.DataFrame:
    """
    Load GDP data from an Excel file.

    Parameters
    ----------
    path : str
        Path to the Excel file containing GDP data.

    Returns
    -------
    pd.DataFrame
        DataFrame with GDP data loaded from the file.
    """
    df = pd.read_excel(path)
    return df


def clean_gdp_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess GDP data.

    Parameters
    ----------
    df : pd.DataFrame
        Raw GDP data DataFrame.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with handled missing values and log
        transformations.
    """
    df_clean = df.copy()

    # Handle missing values with mean imputation
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_clean[col].isnull().sum() > 0:
            df_clean[col].fillna(df_clean[col].mean(), inplace=True)

    # Log transformation for GDP columns
    gdp_cols = [col for col in numeric_cols if col != 'Year']
    for col in gdp_cols:
        if (df_clean[col] > 0).all():
            df_clean[f'log_{col}'] = np.log(df_clean[col])

    return df_clean


def get_data_summary(df: pd.DataFrame) -> dict[str, Any]:
    """
    Get basic data summary.

    Parameters
    ----------
    df : pd.DataFrame
        GDP data DataFrame.

    Returns
    -------
    dict[str, Any]
        Dictionary containing summary statistics including shape,
        columns, missing values, and numeric statistics.
    """
    summary = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_stats': df.describe()
    }
    return summary
