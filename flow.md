1 - download_data.py

2 - load_data.py

3 - train_test_split.py

4 - data_cleaning.py

5 - feature_engineering.py



from src.load_data import get_dataframe
from src.train_test_split import split_data
from src.cleaning import data_cleaning_pipeline
from src.feature_engineering import feature_engineering_pipeline
from src.model import train_model, evaluate_model

def main():
    # Load full raw data
    df = get_dataframe()

    # Split raw data into train/test CSV files (if not done already)
    split_data()

    # Read train and test sets (raw)
    train_df = pd.read_csv('data/train.csv')
    test_df = pd.read_csv('data/test.csv')

    # Fit cleaning & feature engineering pipelines on train only
    train_clean = data_cleaning_pipeline(train_df)
    train_feat = feature_engineering_pipeline(train_clean, fit=True)

    # Apply cleaning & feature engineering to test (without fitting)
    test_clean = data_cleaning_pipeline(test_df)
    test_feat = feature_engineering_pipeline(test_clean, fit=False)

    # Train model on processed train data
    model = train_model(train_feat)

    # Evaluate model on processed test data
    evaluate_model(model, test_feat)

if __name__ == "__main__":
    main()

