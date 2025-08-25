import pandas as pd
import os

def get_dataframe():
    # Get the absolute path to the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate up to the project root
    project_root = os.path.abspath(os.path.join(current_dir, ".."))

    # Construct the full path to the CSV
    file_path = os.path.join(project_root, "data", "raw_original_data.csv")

    print("Looking for file at:", file_path)

    df = pd.read_csv(file_path)
    
    return df

