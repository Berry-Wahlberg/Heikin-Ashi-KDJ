# Heikin-Ashi & KDJ Indicator Analysis
[English](README.md) | [简体中文 Chinese](README_zh-CN.md) | [日本語 Japanese](README_JP.md)
## Overview
This project processes stock OHLC (Open, High, Low, Close) data by the following steps:
1. Converting standard OHLC data into Heikin-Ashi candlesticks.
2. Computing the KDJ indicator values.
3. Identifying buy/sell signals based on J line crossovers.
4. Visualizing the KDJ indicator with buy/sell markers.
5. Outputting trade signals to `Output.csv`.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install pandas numpy matplotlib mplfinance
```

## File Structure
- `Data.csv`: Input file containing OHLC stock data.
- `heikin_ashi_kdj.py`: Main script for processing and analyzing data.
- `Chart.py`: Script for plotting candlestick charts with buy/sell signals.
- `Output.csv`: Generated file with KDJ values and trade signals.

## Usage
First, run the `heikin_ashi_kdj.py` script. It will read `Data.csv`, process Heikin-Ashi candles, compute KDJ values, plot the KDJ indicator with buy/sell markers, and save the signals in `Output.csv`.

```bash
python heikin_ashi_kdj.py
```

Then, run the `Chart.py` script. It will read `Output.csv` and `Data.csv`, and plot a candlestick chart with buy/sell signals.

```bash
python Chart.py
```

## Output Explanation
- **K, D, J**: KDJ indicator values.
- **Signal**:
  - `1` → Buy signal (J crosses above K)
  - `-1` → Sell signal (J crosses below K)
  - `0` → No signal

## Example Output (Output.csv)
| Date       | K    | D    | J    | Signal |
|------------|------|------|------|--------|
| 2024-02-01 | 50.2 | 48.1 | 52.5 | 1      |
| 2024-02-02 | 55.3 | 50.9 | 60.0 | 0      |
| 2024-02-03 | 45.8 | 47.2 | 42.0 | -1     |

## Visualization
The `heikin_ashi_kdj.py` script generates a plot with KDJ lines and marks buy/sell points. The `Chart.py` script generates a candlestick chart with buy/sell signals.

## License
This project is licensed under the MIT License.