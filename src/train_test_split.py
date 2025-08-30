import pandas as pd
from sklearn.model_selection import train_test_split
import os

def split_data(test_size=0.2, random_state=42):
    # Get the absolute path to the directory where this file is located (src/)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate up to the project root from src/
    project_root = os.path.abspath(os.path.join(current_dir, ".."))

    # Construct paths to the data folder
    data_dir = os.path.join(project_root, "data")
    raw_file_path = os.path.join(data_dir, "raw_original_data.csv")
    train_path = os.path.join(data_dir, "train.csv")
    test_path = os.path.join(data_dir, "test.csv")

    # Check file exists
    if not os.path.exists(raw_file_path):
        raise FileNotFoundError(f"Raw data file not found at {raw_file_path}")

    # Load and split
    df = pd.read_csv(raw_file_path)
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)

    # Save
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    print(f"✅ Train and test sets saved to:\n - {train_path}\n - {test_path}")

# Run when executed directly
if __name__ == "__main__":
    split_data()

# Usage:
# From your project root directory, run:
# python src/train_test_split.py
