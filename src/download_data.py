import kaggle 

dataset_path = 'blastchar/telco-customer-churn'

download_path = 'data'

kaggle.api.dataset_download_files(dataset_path, path=download_path, unzip=True)