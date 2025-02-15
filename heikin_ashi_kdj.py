import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read OHLC data
def read_csv(filename):
    """
    Read a CSV file using pandas.

    Args:
        filename (str): The name of the CSV file to be read.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(filename)

# Convert to Heikin-Ashi
def heikin_ashi(df):
    """
    Convert the given DataFrame to Heikin-Ashi format.

    Args:
        df (pd.DataFrame): The original DataFrame containing OHLC data.

    Returns:
        pd.DataFrame: A new DataFrame with Heikin-Ashi data.
    """
    ha_df = df.copy()
    # Calculate the Heikin-Ashi Close price
    ha_df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    # Initialize the Heikin-Ashi Open price with NaN
    ha_df['HA_Open'] = np.nan
    # Calculate the first Heikin-Ashi Open price
    ha_df.loc[0, 'HA_Open'] = (df.loc[0, 'Open'] + df.loc[0, 'Close']) / 2
    # Calculate the remaining Heikin-Ashi Open prices
    for i in range(1, len(df)):
        ha_df.loc[i, 'HA_Open'] = (ha_df.loc[i-1, 'HA_Open'] + ha_df.loc[i-1, 'HA_Close']) / 2
    # Calculate the Heikin-Ashi High price
    ha_df['HA_High'] = ha_df[['HA_Open', 'HA_Close', 'High']].max(axis=1)
    # Calculate the Heikin-Ashi Low price
    ha_df['HA_Low'] = ha_df[['HA_Open', 'HA_Close', 'Low']].min(axis=1)
    return ha_df

# Compute KDJ indicator
def kdj(df, n=9, smooth_k=3, smooth_d=3):
    """
    Compute the KDJ indicator for the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing OHLC data.
        n (int, optional): The period for calculating the lowest low and highest high. Defaults to 9.
        smooth_k (int, optional): The smoothing period for K. Defaults to 3.
        smooth_d (int, optional): The smoothing period for D. Defaults to 3.

    Returns:
        pd.DataFrame: A DataFrame containing the KDJ values.
    """
    # Calculate the lowest low over the given period
    df['Lowest_Low'] = df['Low'].rolling(n).min()
    # Calculate the highest high over the given period
    df['Highest_High'] = df['High'].rolling(n).max()
    # Calculate the RSV value
    df['RSV'] = (df['Close'] - df['Lowest_Low']) / (df['Highest_High'] - df['Lowest_Low']) * 100
    # Calculate the K value using exponential weighted mean
    df['K'] = df['RSV'].ewm(span=smooth_k).mean()
    # Calculate the D value using exponential weighted mean
    df['D'] = df['K'].ewm(span=smooth_d).mean()
    # Calculate the J value
    df['J'] = 3 * df['K'] - 2 * df['D']
    return df[['K', 'D', 'J']]

# Identify buy/sell signals
def trade_signals(df):
    """
    Identify buy and sell signals based on the KDJ indicator.

    Args:
        df (pd.DataFrame): The DataFrame containing KDJ values.

    Returns:
        pd.DataFrame: A DataFrame containing the J, K, D values and the buy/sell signals.
    """
    # Initialize the signal column with 0
    df['Signal'] = 0
    # Set the signal to 1 (buy) when the J crosses above K
    df.loc[(df['J'].shift(1) < df['K'].shift(1)) & (df['J'] > df['K']), 'Signal'] = 1  # Buy
    # Set the signal to -1 (sell) when the J crosses below K
    df.loc[(df['J'].shift(1) > df['K'].shift(1)) & (df['J'] < df['K']), 'Signal'] = -1  # Sell
    return df[['J', 'K', 'D', 'Signal']]

# Plot KDJ and signals
def plot_kdj(df):
    """
    Plot the KDJ indicator and buy/sell signals.

    Args:
        df (pd.DataFrame): The DataFrame containing KDJ values and signals.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['K'], label='K', color='blue')
    plt.plot(df.index, df['D'], label='D', color='orange')
    plt.plot(df.index, df['J'], label='J', color='red')
    
    buy_signals = df[df['Signal'] == 1]
    sell_signals = df[df['Signal'] == -1]
    plt.scatter(buy_signals.index, buy_signals['J'], marker='^', color='green', label='Buy', alpha=1)
    plt.scatter(sell_signals.index, sell_signals['J'], marker='v', color='red', label='Sell', alpha=1)
    
    plt.legend()
    plt.title("KDJ Indicator with Buy/Sell Signals")
    plt.show()

# Save results to CSV
def save_to_csv(df, filename):
    """
    Save the given DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to be saved.
        filename (str): The name of the CSV file to save to.
    """
    df.to_csv(filename, index=False)

# Main function
def main():
    """
    The main function to execute the data processing and analysis.
    """
    data = read_csv("Data.csv")
    ha_data = heikin_ashi(data)
    kdj_data = kdj(ha_data)
    signals = trade_signals(kdj_data)
    plot_kdj(signals)
    save_to_csv(signals, "Output.csv")

if __name__ == "__main__":
    main()