import pandas as pd
import requests
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os

# Function to fill missing data
def clean_data(df):
    # Remove unnecessary columns
    column_drop = [
        'platform.id', 'platform.name', 'platform.symbol', 'platform.slug', 'platform.token_address',
        'tags', 'max_supply', 'circulating_supply', 'total_supply', 'tvl_ratio', 
        'self_reported_market_cap', 'self_reported_circulating_supply', 
        'quote.USD.fully_diluted_market_cap'
    ]
    
    # Drop the unnecessary columns
    df.drop(column_drop, axis=1, inplace=True, errors='ignore')

    # If there are NaN values in the dataset, fill them
    if df.isnull().values.any():
        print("Missing data found, filling in...")
        # Fill the relevant columns with their average
        df['quote.USD.price'] = df['quote.USD.price'].fillna(df['quote.USD.price'].mean())
        df['quote.USD.market_cap'] = df['quote.USD.market_cap'].fillna(df['quote.USD.market_cap'].mean())
    else:
        print("No missing data were found.")
    
    return df

# Function to fetch data from the API
def get_crypto_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'Insert your API key here',
    }

    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters, headers=headers)
        data = json.loads(response.text)
        
        # Convert the API response data to a DataFrame
        df_new = pd.json_normalize(data['data'])
        print("Data successfully retrieved")

        # Add timestamp to the fetched data
        df_new['timestamp'] = pd.to_datetime('now')  # Adding a timestamp
        
        return df_new  # Returning the raw data without cleaning
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return None

# Function to merge new raw (plain) data with the old raw data
def merge_plain_data(df_new, plain_file_path):
    try:
        # If there is no plain data file, just save the new data
        if not os.path.exists(plain_file_path):
            df_new.to_csv(plain_file_path, index=False)
            print(f"Plain data saved to {plain_file_path}.")
        else:
            # Read old plain data and merge it with new data
            df_old = pd.read_csv(plain_file_path)
            df_combined = pd.concat([df_old, df_new], ignore_index=True)
            df_combined.to_csv(plain_file_path, index=False)
            print(f"Plain data merged with old data and saved to {plain_file_path}.")
    except Exception as e:
        print(f"File could not be created or saved: {e}")

# Function to save the cleaned data (overwrite previous clean data)
def save_clean_data(df_new_clean, clean_file_path):
    try:
        # Save the cleaned data (overwrite any existing clean data)
        if os.path.exists(clean_file_path):
            os.remove(clean_file_path)  # Remove the old clean data file if it exists
            print(f"Old cleaned data removed")

        df_new_clean.to_csv(clean_file_path, index=False)
        print(f"Cleaned data saved")
    except Exception as e:
        print(f"Error saving cleaned data")

# Main Function
def run_data_collection(plain_file_path, clean_file_path):
    # Fetch the raw data
    df_new = get_crypto_data()

    # If data is retrieved, save plain (raw) data first
    if df_new is not None:
        # First, save the plain data (append new data to existing)
        merge_plain_data(df_new, plain_file_path)

        # Clean the data by reading it from the saved plain CSV
        df_new_clean = clean_data(df_new)  # Cleaning process is applied directly to the fetched data

        # Save the cleaned data (overwrite the old clean data)
        save_clean_data(df_new_clean, clean_file_path)

# File paths
plain_file_path = r'C:\Users\sarp_\Desktop\X\Data Analyst\Data_Analyst_Projects\crypto_automation\data\plain_crypto_data.csv'
clean_file_path = r'C:\Users\sarp_\Desktop\X\Data Analyst\Data_Analyst_Projects\crypto_automation\data\clean_crypto_data.csv'

# Ensure the directories exist
os.makedirs(os.path.dirname(plain_file_path), exist_ok=True)
os.makedirs(os.path.dirname(clean_file_path), exist_ok=True)

# Run data retrieval and save to file
run_data_collection(plain_file_path, clean_file_path)
