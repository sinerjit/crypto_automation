from data_analysis import read_data, filter_data, calculate_trend_analysis, print_coin_data, calculate_price_volatility
from data_collector import run_data_collection  # Call the data collection function
from data_visualization import plot_price_time_series, plot_market_cap  # Import the visualization functions

# File paths for data
plain_file_path = r'PLAIN_FILE_PATH'
clean_file_path = r'CLEAN_FILE_PATH'

# Main function
def main():
    while True:
        # Get input from the user
        crypto_symbol = input("Please enter a crypto symbol (e.g., BTC) or 'All' for all data (type 'exit' to quit): ").strip()

        # Exit condition
        if crypto_symbol.lower() == 'exit':
            print("Exiting the program.")
            break

        # Start data collection after user input
        print("Fetching and cleaning data...")
        run_data_collection(plain_file_path, clean_file_path)  # Data fetching and cleaning process

        # Data collection completed
        print("Data collection completed. Now performing analysis...")

        # Read the most recent cleaned data
        df = read_data(clean_file_path)

        # Filter the data based on the input symbol
        filtered_data = filter_data(df, crypto_symbol)

        # Check if data exists
        if filtered_data.empty:
            print(f"No data found for symbol: {crypto_symbol.upper()}")
        else:
            # Calculate the average percentage change
            average_percent_change = calculate_trend_analysis(filtered_data)

            # Calculate price volatility
            price_volatility = calculate_price_volatility(filtered_data)

            # If 'All' is entered, print all coins sequentially (no visualization)
            if crypto_symbol.lower() == 'all':
                for i, row in filtered_data.iterrows():
                    print_coin_data(row, average_percent_change.iloc[i], price_volatility.iloc[i])
            else:
                # Print results for a single coin
                row = filtered_data.iloc[0]
                # Print analysis output
                print_coin_data(row, average_percent_change.iloc[0], price_volatility.iloc[0])

                # Display visualizations
                print("\nGenerating visualizations...")
                plot_price_time_series(df, crypto_symbol)
                plot_market_cap(df, crypto_symbol)

# If this file is run directly, call the main function
if __name__ == "__main__":
    main()
