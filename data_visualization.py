import pandas as pd
import matplotlib.pyplot as plt

# Read data from the cleaned file
def read_clean_data(file_path):
    return pd.read_csv(file_path)

# Time series line chart: Visualizing price percentage changes
def plot_price_time_series(df, symbol):
    # Filter data for the selected symbol
    df_symbol = df[df['symbol'] == symbol.upper()]

    # Percentage change data
    time_periods = ['24h', '7d', '30d', '60d', '90d']
    price_changes = [
        df_symbol['quote.USD.percent_change_24h'].values[0],
        df_symbol['quote.USD.percent_change_7d'].values[0],
        df_symbol['quote.USD.percent_change_30d'].values[0],
        df_symbol['quote.USD.percent_change_60d'].values[0],
        df_symbol['quote.USD.percent_change_90d'].values[0]
    ]

    # Create line chart
    plt.figure(figsize=(10, 6))
    plt.plot(time_periods, price_changes, marker='o', linestyle='-', color='b', label=f'{symbol} Price Change')
    plt.title(f'{symbol} Price Time Series', fontsize=14)
    plt.xlabel('Time Periods')
    plt.ylabel('Percentage Change (%)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Market cap chart: Visualizing the market capitalization of the cryptocurrency
def plot_market_cap(df, symbol):
    # Filter data for the selected symbol
    df_symbol = df[df['symbol'] == symbol.upper()]

    # Market Cap and Market Dominance
    market_cap = df_symbol['quote.USD.market_cap'].values[0]
    market_cap_dominance = df_symbol['quote.USD.market_cap_dominance'].values[0]

    # Create bar chart
    plt.figure(figsize=(8, 5))
    plt.bar([symbol], [market_cap], color='c', label=f'{symbol} Market Cap')
    plt.title(f'{symbol} Market Cap', fontsize=14)
    plt.ylabel('Market Cap (USD)')
    plt.grid(True)

    # Add dominance percentage as text
    plt.text(0, market_cap/2, f'Dominance: {market_cap_dominance:.2f}%', fontsize=12, color='red', ha='center')
    plt.legend()
    plt.show()

# if __name__ == "__main__":
#     # Read cleaned data
#     file_path = r'C:\Users\sarp_\Desktop\X\Data Analyst\Data_Analyst_Projects\crypto_automation\data\clean_crypto_data.csv'
#     df = read_clean_data(file_path)

#     # Test with a specific symbol (e.g., BTC)
#     symbol = 'BTC'

#     # Generate Price Time Series and Market Cap charts
#     plot_price_time_series(df, symbol)
#     plot_market_cap(df, symbol)
