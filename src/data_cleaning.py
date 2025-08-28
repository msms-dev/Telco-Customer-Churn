import pandas as pd
import numpy as np

# Handling naming conventions
def replace_service_values(df, columns, values_to_replace=None, replacement_value='No'):
    if values_to_replace is None:
        values_to_replace = ['No internet service', 'No phone service']

    for col in columns:
        df.loc[:, col] = df[col].replace(values_to_replace, replacement_value)

    return df

# Converting column type to numeric 
def convert_column_to_numeric(df, column_name):
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    return df

# Remove missing values
def remove_missing_values(df,column_name):
    df = df[df[column_name].notna()]
    return df



def data_cleaning_pipeline(df):

    # Handling Naming 
    matching_columns = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'MultipleLines']
    df = replace_service_values(df, matching_columns)
    # Convert to Numeric
    convert_column_to_numeric(df, column_name='TotalCharges')
    # Missing values
    df = remove_missing_values(df,column_name='TotalCharges')

    return df


    # To run:
        # df_clean = data_cleaning.clean_transform_pipeline(df)


