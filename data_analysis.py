import pandas as pd

# Read data from the file
def read_data(file_path):
    return pd.read_csv(file_path)

# Filter data by symbol or return all data
def filter_data(df, crypto_symbol):
    if crypto_symbol.lower() == 'all':
        return df  # Return all data
    else:
        # Filter for a specific symbol
        return df[df['symbol'] == crypto_symbol.upper()]

# Calculate trend analysis and return only the values
def calculate_trend_analysis(df):
    # Select relevant columns
    trend_columns = [
        'quote.USD.percent_change_24h',
        'quote.USD.percent_change_7d',
        'quote.USD.percent_change_30d',
        'quote.USD.percent_change_60d',
        'quote.USD.percent_change_90d'
    ]
    
    # Calculate the average percentage change for each coin
    average_percent_change = df[trend_columns].mean(axis=1)
    
    return average_percent_change

# Calculate price volatility
def calculate_price_volatility(df):
    # Select percentage change columns to calculate price changes
    price_change_columns = [
        'quote.USD.percent_change_24h',
        'quote.USD.percent_change_7d',
        'quote.USD.percent_change_30d',
        'quote.USD.percent_change_60d',
        'quote.USD.percent_change_90d'
    ]
    
    # Calculate price volatility using standard deviation
    price_volatility = df[price_change_columns].std(axis=1)
    
    return price_volatility

# Print data for a specific coin
def print_coin_data(row, average_percent_change, price_volatility):
    name = row['name']
    symbol = row['symbol']
    price = row['quote.USD.price']
    market_cap = row['quote.USD.market_cap']
    
    price = round(price, 2)
    market_cap = round(market_cap, 2)

    print(f"\n{name} ({symbol})")
    print(f"Current price: {price}")
    print(f"Market cap: {market_cap}")
    print(f"Average Percentage Change: %{average_percent_change:.2f}")
    print(f"Price Volatility: %{price_volatility:.2f}")
