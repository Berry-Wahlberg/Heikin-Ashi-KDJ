import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# 读取CSV文件，将Date列解析为日期格式并设置为索引列
def read_csv_file(filename):
    try:
        return pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
    except FileNotFoundError:
        print(f"文件 {filename} 未找到，请检查文件路径。")
        return None
    except Exception as e:
        print(f"读取文件 {filename} 时出现错误：{e}")
        return None

# Plot candlestick chart with buy/sell signals
def plot_trading_chart(df, data_csv, figsize=(12, 6), style='charles'):
    # Read original OHLC data for candlestick plot
    ohlc_data = read_csv_file(data_csv)
    if ohlc_data is None:
        return
    ohlc_data = ohlc_data[['Open', 'High', 'Low', 'Close']]
    
    # Extract buy/sell signals
    buy_signals = df[df['Signal'] == 1]
    sell_signals = df[df['Signal'] == -1]
    
    # Convert signals to matplotlib format
    buy_dates = buy_signals.index
    sell_dates = sell_signals.index
    buy_prices = ohlc_data.loc[buy_dates, 'Close']
    sell_prices = ohlc_data.loc[sell_dates, 'Close']
    
    # Plot candlestick chart
    fig, ax = plt.subplots(figsize=figsize)
    mpf.plot(ohlc_data, type='candle', style=style, ax=ax)
    
    # Plot buy/sell signals
    ax.scatter(buy_dates, buy_prices, marker='^', color='g', label='Buy', alpha=1, zorder=3)
    ax.scatter(sell_dates, sell_prices, marker='v', color='r', label='Sell', alpha=1, zorder=3)
    
    ax.legend()
    plt.title("Trading Positions on Candlestick Chart")
    plt.show()

# Main function
def main():
    output_df = read_csv_file("Output.CSV")
    if output_df is not None:
        plot_trading_chart(output_df, "DATA.CSV")

if __name__ == "__main__":
    main()