import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read OHLC data
def read_csv(filename):
    return pd.read_csv(filename)

# Convert to Heikin-Ashi
def heikin_ashi(df):
    ha_df = df.copy()
    ha_df['HA_Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    ha_df['HA_Open'] = np.nan
    ha_df.loc[0, 'HA_Open'] = (df.loc[0, 'Open'] + df.loc[0, 'Close']) / 2
    for i in range(1, len(df)):
        ha_df.loc[i, 'HA_Open'] = (ha_df.loc[i-1, 'HA_Open'] + ha_df.loc[i-1, 'HA_Close']) / 2
    ha_df['HA_High'] = ha_df[['HA_Open', 'HA_Close', 'High']].max(axis=1)
    ha_df['HA_Low'] = ha_df[['HA_Open', 'HA_Close', 'Low']].min(axis=1)
    return ha_df

# Compute KDJ indicator
def kdj(df, n=9, smooth_k=3, smooth_d=3):
    df['Lowest_Low'] = df['Low'].rolling(n).min()
    df['Highest_High'] = df['High'].rolling(n).max()
    df['RSV'] = (df['Close'] - df['Lowest_Low']) / (df['Highest_High'] - df['Lowest_Low']) * 100
    df['K'] = df['RSV'].ewm(span=smooth_k).mean()
    df['D'] = df['K'].ewm(span=smooth_d).mean()
    df['J'] = 3 * df['K'] - 2 * df['D']
    return df[['K', 'D', 'J']]

# Identify buy/sell signals
def trade_signals(df):
    df['Signal'] = 0
    df.loc[(df['J'].shift(1) < df['K'].shift(1)) & (df['J'] > df['K']), 'Signal'] = 1  # Buy
    df.loc[(df['J'].shift(1) > df['K'].shift(1)) & (df['J'] < df['K']), 'Signal'] = -1  # Sell
    return df[['J', 'K', 'D', 'Signal']]

# Plot KDJ and signals
def plot_kdj(df):
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
    df.to_csv(filename, index=False)

# Main function
def main():
    data = read_csv("Data.csv")
    ha_data = heikin_ashi(data)
    kdj_data = kdj(ha_data)
    signals = trade_signals(kdj_data)
    plot_kdj(signals)
    save_to_csv(signals, "Output.csv")

if __name__ == "__main__":
    main()
