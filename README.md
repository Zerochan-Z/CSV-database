# 📘 Crypto Market Simulation – Short Reference

One‑line explanations.  
Replace `(value)`, `[index]`, `"name"` with your own data.

---

## 📁 File / Path

| Code | What it does |
|------|--------------|
| `import pandas as pd` | Load pandas (Excel‑like tables). |
| `import numpy as np` | Load numpy (fast math & random numbers). |
| `import matplotlib.pyplot as plt` | Load plotting tools. |
| `import os` | Operating system functions (e.g. file existence check). {os.path.exists()} |

## 🐼 Pandas

| Code | Meaning |
|------|---------|
| `pd.read_csv("file.csv")` | Load CSV into a DataFrame. |
| `df.head(n)` | First `n` rows. |
| `df.tail(n)` | Last `n` rows. |
| `df.shape` | `(rows, columns)`. |
| `df.shape[0]` | Number of rows. |
| `df.shape[1]` | Number of columns. |
| `df.columns` | Column names. |
| `df.to_csv("file.csv", index=False)` | Save CSV; no extra index column. |
| `df.round({"Col": decimals})` | Round column(s) to `decimals`. |

## 🔢 NumPy

| Code | Meaning |
|------|---------|
| `np.random.seed(integer)` | Fix random sequence. |
| `np.random.uniform(low, high, size)` | Random floats between `low` and `high`. |
| `np.random.randint(low, high, size, dtype)` | Random integers `low` to `high-1`. |
| `np.random.normal(mean, std, size)` | Normal distribution numbers. |
| `np.cumprod(array)` | Cumulative product. |
| `np.cumsum(array)` | Cumulative sum. [works with .exp to form {multiplier}] |
| `np.exp(array)` | Exponential. {e^(array)} |
| `np.maximum(a, b)` | Element‑wise max. |
| `np.minimum(a, b)` | Element‑wise min. |
| `np.abs(array)` | No negative num for multiplier always be linked with .max/.min |
| `np.zeros(length)` | Creates array {datas} to store (days) |

## 📈 Price Simulation (Random Walk)

| Code | Meaning |
|------|---------|
| `starting_price = value` | First day's price. |
| `daily_returns = np.random.uniform(min, max, days)` | Daily changes in % (decimal). |
| `price_path = start * np.cumprod(1 + returns)` | Closing price path. |
| `percentage_returns = returns * 100` | Decimals → percentages. |
| `open_prices[i] = closed_prices[i-1]` | Today's open = yesterday's close. |
| `close = open * (1 + random_move)` | Intraday move to get close. |
| `high = max(open,close) * (1 + positive_random)` | -> A rule
| `low = min(open,close) * (1 - positive_random)` | --> A rule
| `volume = np.random.randint(low, high, days, dtype=np.int64)` | Random integer volume. |

## 📊 Matplotlib (Plotting)

| Code | Meaning |
|------|---------|
| `plt.figure(figsize=(width, height))` | Chart size in inches. |
| `plt.plot(x, y, label="text")` | Line plot. |
| `df["Column"]` | Select a column. |
| `plt.title("text", fontsize=n, fontweight="bold")` | Title. |
| `plt.xlabel("text")` | X‑axis label. |
| `plt.ylabel("text")` | Y‑axis label. |
| `plt.xticks(positions, rotation=deg)` | Tick positions and rotation. |
| `plt.grid(True, linestyle="--", alpha=0.5)` | Dashed grid, half transparent. |
| `plt.legend(loc="position")` | Legend box. |
| `plt.tight_layout()` | Fix overlapping labels. |
| `plt.show()` | Display chart. |

## ⚠️ Error Handling

| Code | Meaning |
|------|---------|
| `try: ... except FileNotFoundError:` | Catch missing file error. |
| `except Exception as e:` | Catch any error. |

---

*Replace placeholders (`value`, `min`, `max`, `"text"`, etc.) with your actual data.*
