# Crypto Automation

A Python-based automation project for cryptocurrency data collection, analysis, and visualization using the CoinMarketCap API. This project provides insights like price trends, market capitalization, and price volatility.

---

## Overview

The **Crypto Automation** project focuses on:
- Collecting cryptocurrency data from the CoinMarketCap API.
- Cleaning and organizing the collected data for analysis.
- Analyzing trends such as price changes and market volatility.
- Visualizing data for better understanding and interpretation.

---

## Features
- **Data Collection**: Fetch cryptocurrency data such as price, market cap, and percent changes.
- **Data Cleaning**: Organize and clean raw data, filling missing values where necessary.
- **Trend Analysis**: Calculate average price changes and price volatility.
- **Visualization**: Generate time-series plots and market cap comparisons.

---

## Project Structure
```
crypto_automation/ 
├── .gitignore                               # Excluded files and directories 
├── requirements.txt                         # Python dependencies 
├── data_analysis.py                         # Data analysis functions 
├── data_collector.py                        # Data collection and cleaning 
├── data_visualization.py                    # Data visualization functions 
├── main.py                                  # Main script to run the project
```
---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or above
- A CoinMarketCap API key

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sinerjit/crypto_automation.git
   cd crypto_automation
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Add your CoinMarketCap API key: Open data_collector.py and replace 'Insert your API key here' with your API key:
   ```bash
   headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'Insert your API key here',
   }


## How to Run
1. Run the main script:
   ```bash
   python main.py
2. Follow the prompts to enter a cryptocurrency symbol (e.g., BTC for Bitcoin) or select "All" for analyzing all available data.
3. View generated insights and visualizations.

## Visualizations
1. Time-Series Graphs: Show percentage price changes over time.
2. Market Cap Comparison: Highlight cryptocurrency market dominance and value.
