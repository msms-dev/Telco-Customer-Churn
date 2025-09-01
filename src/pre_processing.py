import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

def one_hot_encode(df, exclude_columns=None, drop_first=True):
    if exclude_columns is None:
        exclude_columns = []

    # Identify categorical columns to encode
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    cat_cols = [col for col in cat_cols if col not in exclude_columns]

    # Apply one-hot encoding
    df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=drop_first)

    return df_encoded

def convert_boolean_like_columns(df):
    df = df.copy()

    for col in df.columns:
        unique_vals = df[col].dropna().unique()

        # Handle 'Yes' / 'No'
        if set(unique_vals).issubset({'Yes', 'No'}):
            df[col] = df[col].map({'Yes': 1, 'No': 0})
        
        # Handle True / False (bool)
        elif df[col].dtype == bool:
            df[col] = df[col].astype(int)

        # Also handle object columns that contain actual bools
        elif set(unique_vals).issubset({True, False}):
            df[col] = df[col].astype(int)

    return df


# Create function to scale the features, with optional different types

def scale_continuous_features(df, scaler_type='minmax'):
    df = df.copy()

    # Choose scaler
    scaler_dict = {
        'minmax': MinMaxScaler(),
        'standard': StandardScaler(),
        'robust': RobustScaler()
    }
    if scaler_type not in scaler_dict:
        raise ValueError("scaler_type must be one of: 'minmax', 'standard', 'robust'")
    
    scaler = scaler_dict[scaler_type]

    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # Separate binary and continuous numeric columns
    binary_cols = [col for col in numeric_cols if df[col].nunique() == 2]
    continuous_cols = [col for col in numeric_cols if col not in binary_cols]

    # Apply scaler to continuous columns only
    df[continuous_cols] = scaler.fit_transform(df[continuous_cols])

    return df, scaler


def pre_processing_pipelines(df):

    exclude_columns=['customerID', 'Churn']
    scaler_type='minmax'

    df = one_hot_encode(df, exclude_columns=exclude_columns)
    df = convert_boolean_like_columns(df)
    df, fitted_scaler = scale_continuous_features(df, scaler_type=scaler_type)

    return df