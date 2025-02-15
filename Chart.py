import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Read a CSV file, parse the 'Date' column as a date format and set it as the index column
def read_csv_file(filename):
    try:
        # Try to read the CSV file with specified date parsing and index setting
        return pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
    except FileNotFoundError:
        # If the file is not found, print an error message and return None
        print(f"File {filename} not found. Please check the file path.")
        return None
    except Exception as e:
        # If other errors occur during reading, print the error message and return None
        print(f"An error occurred while reading file {filename}: {e}")
        return None

# Plot a candlestick chart with buy/sell signals
def plot_trading_chart(df, data_csv, figsize=(12, 6), style='charles'):
    # Read original OHLC (Open, High, Low, Close) data for the candlestick plot
    ohlc_data = read_csv_file(data_csv)
    if ohlc_data is None:
        # If the data is not successfully read, return early
        return
    # Select only the necessary columns for the candlestick plot
    ohlc_data = ohlc_data[['Open', 'High', 'Low', 'Close']]

    # Extract buy/sell signals
    # Select rows where the 'Signal' column is 1 (buy signals)
    buy_signals = df[df['Signal'] == 1]
    # Select rows where the 'Signal' column is -1 (sell signals)
    sell_signals = df[df['Signal'] == -1]

    # Convert signals to matplotlib format
    # Get the dates of the buy signals
    buy_dates = buy_signals.index
    # Get the dates of the sell signals
    sell_dates = sell_signals.index
    # Get the closing prices corresponding to the buy signal dates
    buy_prices = ohlc_data.loc[buy_dates, 'Close']
    # Get the closing prices corresponding to the sell signal dates
    sell_prices = ohlc_data.loc[sell_dates, 'Close']

    # Plot candlestick chart
    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=figsize)
    # Plot the candlestick chart using mplfinance
    mpf.plot(ohlc_data, type='candle', style=style, ax=ax)

    # Plot buy/sell signals
    # Plot buy signals as green upward triangles
    ax.scatter(buy_dates, buy_prices, marker='^', color='g', label='Buy', alpha=1, zorder=3)
    # Plot sell signals as red downward triangles
    ax.scatter(sell_dates, sell_prices, marker='v', color='r', label='Sell', alpha=1, zorder=3)

    # Show the legend
    ax.legend()
    # Set the title of the plot
    plt.title("Trading Positions on Candlestick Chart")
    # Display the plot
    plt.show()

# Main function
def main():
    # Read the output data from the CSV file
    output_df = read_csv_file("Output.CSV")
    if output_df is not None:
        # If the data is successfully read, plot the trading chart
        plot_trading_chart(output_df, "DATA.CSV")

if __name__ == "__main__":
    # Call the main function when the script is run directly
    main()