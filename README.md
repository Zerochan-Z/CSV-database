## ✅ README.md – Wencoin Crypto Simulator (Combined)

# 📈 Wencoin Crypto Simulator

A Python program that generates synthetic cryptocurrency price data using a random walk model. Available in two versions: **Interactive (25-day)** with a data viewer menu, and **Non-Interactive (7-day)** for quick preview.

---

## 📋 Program Flow

| Step | Action |
|:----:|--------|
| 1 | Generate synthetic OHLCV data (Open, High, Low, Close, Volume) |
| 2 | Save data to CSV file |
| 3 | Load data from CSV |
| 4 | Display data (interactive menu or full print) |
| 5 | Plot price chart with Matplotlib |

---

## 🧠 Key Code Concepts

| Concept | How it's used |
|---------|----------------|
| `np.random.seed(42)` | Reproducible random numbers |
| `np.random.normal()` | Generate daily returns (log-normal) |
| `np.exp(np.cumsum())` | Create random walk price path |
| `np.maximum()` / `np.minimum()` | Calculate high/low prices with wicks |
| `pd.DataFrame()` | Structure OHLCV data |
| `df.to_csv()` | Save data to CSV |
| `plt.plot()` | Line chart for closing price |
| `plt.xticks(rotation=45)` | Rotate date labels |
| `while True` | Interactive menu loop |
| `try/except` | Error handling for user input |

---

## 📊 Price Simulation Logic

| Component | How it's generated |
|-----------|---------------------|
| **Daily Returns** | Normal distribution (`mean=0.0008`, `std=0.02`) |
| **Open Price** | Previous day's close |
| **Close Price** | `100 × exp(cumsum(returns))` |
| **High Price** | `max(open, close) × (1 + random wick)` |
| **Low Price** | `min(open, close) × (1 - random wick)` |
| **Volume** | Random integer between 300M and 400M |

---

## 📤 Output Examples

### Data Preview
```
         Date   Open   High    Low  Close    Volume  Percentage Return (%)
0  01-05-2026 100.00 101.23  99.45 100.89  345678901                  0.89
1  02-05-2026 100.89 102.12 100.12 101.56  367890123                  0.66
```

### Price Chart
- Blue line showing closing price over time
- X-axis labels rotated 45° for readability
- Dashed grid lines for easier reading

---

## 🧪 Error Handling

| User action | Program response |
|-------------|------------------|
| Requests more rows than available | `Sorry, we only have {days} days of data` |
| Enters non-numeric input | `Please enter a number` |
| File not found | Generates fresh data |
| File exists | Loads existing CSV |

---

## ✅ Key Takeaways

| Concept | How it's used |
|---------|----------------|
| Random walk | Simulates realistic price movement |
| `np.exp(np.cumsum())` | Creates compound growth path |
| `np.maximum()` / `np.minimum()` | Ensures high ≥ open/close, low ≤ open/close |
| `pd.DataFrame()` | Structures OHLCV data |
| `plt.xticks()[::5]` | Show every 5th date for cleaner chart |

---

## 📁 Project Status

| Feature | 7-Day (Non-Interactive) | 25-Day (Interactive) |
|---------|------------------------|----------------------|
| Generate synthetic data | ✅ | ✅ |
| Save to CSV | ✅ | ✅ |
| Load from CSV | ✅ | ✅ |
| Display first N rows | ✅ | ✅ |
| Display last N rows | ❌ | ✅ |
| Price chart | ✅ | ✅ |
| Interactive menu | ❌ | ✅ |
| Error handling | ✅ | ✅ |

---

> *Last updated: June 2026*
```
