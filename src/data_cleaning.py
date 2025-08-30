import pandas as pd
import numpy as np

def replace_service_values(df, columns, values_to_replace=None, replacement_value='No'):
    """
    Replace service-related values like 'No internet service' or 'No phone service' with 'No'.
    """
    if values_to_replace is None:
        values_to_replace = ['No internet service', 'No phone service']

    for col in columns:
        df.loc[:, col] = df[col].replace(values_to_replace, replacement_value)

    return df

def convert_column_to_numeric(df, column_name):
    """
    Convert specified column to numeric type, coercing errors to NaN.
    """
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    return df

def remove_missing_values(df, column_name):
    """
    Remove rows where the specified column has missing values.
    """
    df = df[df[column_name].notna()]
    return df

def data_cleaning_pipeline(df):
    """
    Run the full cleaning pipeline on the DataFrame.
    """
    matching_columns = [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies', 'MultipleLines'
    ]

    df = replace_service_values(df, matching_columns)
    df = convert_column_to_numeric(df, column_name='TotalCharges')
    df = remove_missing_values(df, column_name='TotalCharges')

    return df

# To run:
# import data_cleaning
# df_clean = data_cleaning.data_cleaning_pipeline(df)



