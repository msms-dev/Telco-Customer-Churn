import kaggle
import os
import shutil

# --- 1. Download the dataset ---
dataset_path = 'blastchar/telco-customer-churn'
download_path = 'data'

# Download and unzip the dataset
kaggle.api.dataset_download_files(dataset_path, path=download_path, unzip=True)

# --- 2. Create a duplicate of the raw dataset ---
# Define paths
original_file = os.path.join(download_path, 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
duplicate_file = os.path.join(download_path, 'raw_original_data.csv')

# Copy the file
if os.path.exists(original_file):
    shutil.copyfile(original_file, duplicate_file)
    print(f"✅ Raw copy created: {duplicate_file}")
else:
    print(f"❌ Original file not found at: {original_file}")
