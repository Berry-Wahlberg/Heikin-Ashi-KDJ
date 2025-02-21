# 平均足とKDJインジケーターの分析
[English](README.md) | [简体中文 Chinese](README_zh-CN.md) | [日本語 Japanese](README_JP.md)
## 概要
このプロジェクトは、株式のOHLC（始値、高値、安値、終値）データを以下のステップで処理します。
1. 標準のOHLCデータを平均足ロウソク足に変換する。
2. KDJインジケーターの値を計算する。
3. J線のクロスオーバーに基づいて買い/売りシグナルを特定する。
4. 買い/売りマーカー付きのKDJインジケーターを可視化する。
5. 取引シグナルを `Output.csv` に出力する。

## 必要条件
以下の依存関係がインストールされていることを確認してください。

```bash
pip install pandas numpy matplotlib mplfinance
```

## ファイル構造
- `Data.csv`：OHLC株式データを含む入力ファイル。
- `heikin_ashi_kdj.py`：データの処理と分析を行うメインスクリプト。
- `Chart.py`：買い/売りシグナル付きのロウソク足チャートをプロットするスクリプト。
- `Output.csv`：KDJ値と取引シグナルを含む生成ファイル。

## 使い方
まず、`heikin_ashi_kdj.py` スクリプトを実行します。これにより、`Data.csv` が読み込まれ、平均足ロウソク足が処理され、KDJ値が計算され、買い/売りマーカー付きのKDJインジケーターがプロットされ、シグナルが `Output.csv` に保存されます。

```bash
python heikin_ashi_kdj.py
```

次に、`Chart.py` スクリプトを実行します。これにより、`Output.csv` と `Data.csv` が読み込まれ、買い/売りシグナル付きのロウソク足チャートがプロットされます。

```bash
python Chart.py
```

## 出力の説明
- **K, D, J**：KDJインジケーターの値。
- **Signal**：
  - `1` → 買いシグナル（JがKを上回ってクロス）
  - `-1` → 売りシグナル（JがKを下回ってクロス）
  - `0` → シグナルなし

## 出力例（Output.csv）
| Date       | K    | D    | J    | Signal |
|------------|------|------|------|--------|
| 2024-02-01 | 50.2 | 48.1 | 52.5 | 1      |
| 2024-02-02 | 55.3 | 50.9 | 60.0 | 0      |
| 2024-02-03 | 45.8 | 47.2 | 42.0 | -1     |

## 可視化
`heikin_ashi_kdj.py` スクリプトは、KDJ線と買い/売りポイントをマークしたプロットを生成します。`Chart.py` スクリプトは、買い/売りシグナル付きのロウソク足チャートを生成します。

## ライセンス
このプロジェクトはMITライセンスの下で提供されています。