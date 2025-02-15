# Heikin-Ashi 与 KDJ 指标分析
[English](README.md) | [简体中文 Chinese](README_zh-CN.md) | [日本語 Japanese](README_JP.md)

## 概述
本项目通过以下步骤处理股票的 OHLC（开盘价、最高价、最低价、收盘价）数据：
1. 将标准的 OHLC 数据转换为 Heikin-Ashi 蜡烛图数据。
2. 计算 KDJ 指标值。
3. 基于 J 线交叉情况识别买卖信号。
4. 绘制带有买卖标记的 KDJ 指标图。
5. 将交易信号输出到 `Output.csv` 文件中。

## 依赖要求
请确保已安装以下依赖库：

```bash
pip install pandas numpy matplotlib mplfinance
```

## 文件结构
- `Data.csv`：包含 OHLC 股票数据的输入文件。
- `heikin_ashi_kdj.py`：用于处理和分析数据的主脚本。
- `Chart.py`：用于绘制带有买卖信号的蜡烛图的脚本。
- `Output.csv`：生成的包含 KDJ 值和交易信号的文件。

## 使用方法
首先，运行 `heikin_ashi_kdj.py` 脚本。它会读取 `Data.csv` 文件，处理 Heikin-Ashi 蜡烛图数据，计算 KDJ 值，绘制带有买卖标记的 KDJ 指标图，并将信号保存到 `Output.csv` 文件中。

```bash
python heikin_ashi_kdj.py
```

然后，运行 `Chart.py` 脚本。它会读取 `Output.csv` 和 `Data.csv` 文件，并绘制带有买卖信号的蜡烛图。

```bash
python Chart.py
```

## 输出说明
- **K, D, J**：KDJ 指标值。
- **Signal（信号）**：
  - `1` → 买入信号（J 线上穿 K 线）
  - `-1` → 卖出信号（J 线下穿 K 线）
  - `0` → 无信号

## 输出示例（Output.csv）
| Date       | K    | D    | J    | Signal |
|------------|------|------|------|--------|
| 2024-02-01 | 50.2 | 48.1 | 52.5 | 1      |
| 2024-02-02 | 55.3 | 50.9 | 60.0 | 0      |
| 2024-02-03 | 45.8 | 47.2 | 42.0 | -1     |

## 可视化
`heikin_ashi_kdj.py` 脚本会生成一个包含 KDJ 线和买卖点标记的图表。`Chart.py` 脚本会生成一个带有买卖信号的蜡烛图。

## 许可证
[LICENSE](LICENSE)