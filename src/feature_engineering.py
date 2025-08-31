import pandas as pd
import numpy as np

# Create Bins 
def create_bins(df, columns, bins=5):
    for col in columns:
        bin_col_name = f"{col}_Bin"
        try:
            # Avoid SettingWithCopyWarning
            df.loc[:, bin_col_name] = pd.qcut(df[col], q=bins, duplicates='drop')
            print(f"\nBin counts for {col}:")
            print(df[bin_col_name].value_counts().sort_index())
        except ValueError as e:
            print(f"Could not bin {col}: {e}")
    return df


# Interaction Terms
def add_interaction_with_binary_condition(df, feature_1, feature_2, mask_1=None, mask_2=None):
    # Create masked or raw values
    col1_vals = (df[feature_1] == mask_1).astype(int) if mask_1 is not None else df[feature_1]
    col2_vals = (df[feature_2] == mask_2).astype(int) if mask_2 is not None else df[feature_2]

    # Define new interaction column name
    col1_name = f"{feature_1}_{mask_1}" if mask_1 else feature_1
    col2_name = f"{feature_2}_{mask_2}" if mask_2 else feature_2
    interaction_col = f"{col1_name}_X_{col2_name}"

    # Assign interaction term directly
    df.loc[:, interaction_col] = col1_vals * col2_vals

    return df

def generate_interactions_from_spec(df, interaction_specs):
    for spec in interaction_specs:
        feature_1, feature_2, mask_1, mask_2 = spec
        df = add_interaction_with_binary_condition(df, feature_1, feature_2, mask_1, mask_2)
    
    return df





# Final Pipeline
def feature_engineering_pipeline(df):
    df = df.copy()

    columns_to_bin = ['TotalCharges', 'tenure']
    interaction_specs = [
    ('Contract', 'PaymentMethod', 'Two year', 'Electronic check'),
    ('OnlineSecurity', 'TechSupport', 'No', 'No')
    ]

    df = create_bins(df, columns=columns_to_bin, bins=5)
    df = generate_interactions_from_spec(df, interaction_specs)

    return df

# to run: 
# import feature_engineering
# df_featured = feature_engingeering.feature_engingeering_pipeline(df)