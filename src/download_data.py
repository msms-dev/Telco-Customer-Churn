import kaggle
import os
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))
    download_path = os.path.join(project_root, 'data')

    dataset_path = 'blastchar/telco-customer-churn'

    os.makedirs(download_path, exist_ok=True)

    api = KaggleApi()
    try:
        api.authenticate()
    except Exception as e:
        print("❌ Kaggle API authentication failed.")
        print("Make sure you have your Kaggle API credentials set up correctly.")
        print("Create an API token at https://www.kaggle.com/account, then place kaggle.json in ~/.kaggle/")
        print(f"Error details: {e}")
        return

    try:
        api.dataset_download_files(dataset_path, path=download_path, unzip=True)
        print("✅ Dataset downloaded and unzipped successfully.")
    except Exception as e:
        print("❌ Failed to download dataset from Kaggle.")
        print(f"Error details: {e}")
        return

    original_file = os.path.join(download_path, 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
    duplicate_file = os.path.join(download_path, 'raw_original_data.csv')

    if os.path.exists(original_file):
        shutil.copyfile(original_file, duplicate_file)
        print(f"Raw copy created: {duplicate_file}")
    else:
        print(f"Original file not found at: {original_file}")

if __name__ == "__main__":
    download_dataset()
