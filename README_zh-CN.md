# Heikin-Ashi & KDJ Indicator Analysis

## Overview
此项目用于处理股票的 OHLC（开盘价、最高价、最低价、收盘价）数据，具体步骤如下：
1. 将标准的 OHLC 数据转换为 Heikin-Ashi 蜡烛图数据。
2. 计算 KDJ 指标值。
3. 根据 J 线的交叉情况识别买卖信号。
4. 可视化 KDJ 指标并标记买卖点。
5. 将交易信号输出到 `Output.csv` 文件。

## Requirements
请确保已经安装了以下依赖库：

```bash
pip install pandas numpy matplotlib mplfinance
```

## File Structure
- `Data.csv`：包含 OHLC 股票数据的输入文件。
- `heikin_ashi_kdj.py`：用于处理和分析数据的主脚本。
- `Chart.py`：用于绘制带有买卖信号的蜡烛图的脚本。
- `Output.csv`：生成的包含 KDJ 值和交易信号的文件。

## Usage
首先运行 `heikin_ashi_kdj.py` 脚本，该脚本会读取 `Data.csv` 文件，处理 Heikin-Ashi 蜡烛图数据，计算 KDJ 值，绘制 KDJ 指标图，并将信号保存到 `Output.csv` 文件中。

```bash
python heikin_ashi_kdj.py
```

然后运行 `Chart.py` 脚本，该脚本会读取 `Output.csv` 文件和 `Data.csv` 文件，绘制带有买卖信号的蜡烛图。

```bash
python Chart.py
```

## Output Explanation
- **K, D, J**：KDJ 指标值。
- **Signal**：
  - `1` → 买入信号（J 线上穿 K 线）
  - `-1` → 卖出信号（J 线下穿 K 线）
  - `0` → 无信号

## Example Output (Output.csv)
| Date       | K    | D    | J    | Signal |
|------------|------|------|------|--------|
| 2024-02-01 | 50.2 | 48.1 | 52.5 | 1      |
| 2024-02-02 | 55.3 | 50.9 | 60.0 | 0      |
| 2024-02-03 | 45.8 | 47.2 | 42.0 | -1     |

## Visualization
`heikin_ashi_kdj.py` 脚本会生成一个包含 KDJ 线和买卖点标记的图表，`Chart.py` 脚本会生成一个带有买卖信号的蜡烛图。

## License
此项目基于 MIT 许可证。
