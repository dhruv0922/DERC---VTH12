import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess_data():
    # Load datasets
    housing_data = pd.read_csv('data/housing_data.csv')
    economic_data = pd.read_csv('data/economic_indicators.csv')
    demographic_data = pd.read_csv('data/demographic_data.csv')

    # Merge datasets on region/neighborhood
    merged_data = pd.merge(housing_data, economic_data, on='region')
    merged_data = pd.merge(merged_data, demographic_data, on='region')

    # Fill missing values
    merged_data = merged_data.fillna(method='ffill')

    # Separate features and target
    X = merged_data.drop(['target_column'], axis=1)  # Replace 'target_column' with actual column
    y = merged_data['target_column']

    # Scale features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y
