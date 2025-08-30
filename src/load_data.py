import pandas as pd
import os

def get_dataframe():
    # Get the absolute path to the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate up to the project root (assuming load_data.py is in a subfolder)
    project_root = os.path.abspath(os.path.join(current_dir, ".."))

    # Construct the full path to the CSV
    file_path = os.path.join(project_root, "data", "raw_original_data.csv")

    print(f"Looking for file at: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at {file_path}. Please ensure the data is downloaded.")

    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = get_dataframe()
    print(df.head())


