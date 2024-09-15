import pandas as pd

def load_and_preprocess_data():
    # Load datasets
    housing_data = pd.read_csv('data/housing_data.csv')
    economic_data = pd.read_csv('data/economic_indicators.csv')
    demographic_data = pd.read_csv('data/demographic_data.csv')

    # Print the first few rows to confirm loading
    print("Housing Data:")
    print(housing_data.head())

    print("Economic Data:")
    print(economic_data.head())

    print("Demographic Data:")
    print(demographic_data.head())

    # Merge datasets on region and year
    merged_data = pd.merge(housing_data, economic_data, on=['region', 'year'])
    merged_data = pd.merge(merged_data, demographic_data, on=['region', 'year'])

    # Fill missing values
    merged_data = merged_data.fillna(method='ffill')

    # Separate features and target
    X = merged_data.drop(['median_price'], axis=1)  # Replace 'median_price' with your target column
    y = merged_data['median_price']

    return X, y
