import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. CONFIGURATION & SIMULATION ---
np.random.seed(42)
days = 365
date_range = pd.date_range(start="17-05-2025", periods=days, freq='D')

# Generate the market price path (Random Walk)
daily_returns = np.random.normal(0.0005, 0.015, days)
#writing (normal) distribution -> (mean, standard deviation, size)
#np.random.normal -> generate +/- for you automatically.
#mean (+) -> long-term average daily growth rate
# SD (+/{after np.random.normal generates} >> -) -> combine with mean to check the growth/delay of market
#                                                   restricted between +0.015 < S.D < -0.015
closed_prices = 60000 * np.exp(np.cumsum(daily_returns))
# np.exp = running total scoreboard for each day and translates it into a multiplier
# cumsum = combine daily_returns and determine whether the market growth / delay


# Structure the candlestick components perfectly
open_prices = np.zeros(days)
#Creates array {datas} to store (days) opening prices
open_prices[0] = 60000
for i in range(1, days):
    open_prices[i] = closed_prices[i - 1]
    #open_prices= [yesterday] close_prices

# Force wicks to be structurally sound
high_prices = np.maximum(open_prices, closed_prices) * (1 + np.abs(np.random.normal(0.002, 0.001, days)))
#np.max -> Takes the HIGHER value between open and close for each day
# np.abs -> make sure the numbers are positive
# 1+ (Creates a multiplier slightly above 1)
low_prices = np.minimum(open_prices, closed_prices) * (1 - np.abs(np.random.normal(0.002, 0.001, days)))
random_volume = np.random.randint(30000000000, 40000000000, days,dtype=np.int64)
#Generates random INTEGERS between (a , b)

# Pack everything into the DataFrame
mock_data = pd.DataFrame({
    'Date': date_range.strftime('%d-%m-%Y'),
    'Open': np.round(open_prices, 2),
    'High': np.round(high_prices, 2),
    'Low': np.round(low_prices, 2),
    'Close': np.round(closed_prices, 2),
    'Volume': random_volume,
    'Daily Return (%)': np.round(daily_returns * 100, 2)
})

# Save to text file
file_name = "mock_market_data.csv"
mock_data.to_csv(file_name, index=False)

# --- 2. THE PRICE CHECKER & PLOTTER PIPELINE ---
try:
    # Load the file back in
    df = pd.read_csv(file_name)

    # Run the text health checks in the console
    print("=" * 50)
    print("         DATA PIPELINE HEALTH CHECK            ")
    print("=" * 50)
    print(f"Total Trading Days Processed: {df.shape[0]}")
    #shape -> count how many rows & columns
    #[0,1] -> [rows,columns]
    print(f"Data Schema Columns:          {list(df.columns)}")
    print("-" * 50)
    print("First 3 rows of processed data:")
    print(df[['Date', 'Close', 'Daily Return (%)']].head(3))
    print("=" * 50)

    # --- 3. MATPLOTLIB VISUALIZATION ---
    print("\nLaunching Matplotlib price chart window...")
    plt.figure(figsize=(12, 6))
    #figure -> creates new chart window
    #figsize -> Sets chart size: 12 inches wide, 6 inches tall

    # Plot the asset closing price path
    plt.plot(df['Date'], df['Close'], label='Asset Close Price', color='royalblue', linewidth=2)
    #plt.plot -> starts to design the chart
    #df[    ]  -> Get the Date column

    # Format the look of the chart
    plt.title("Simulated Quantitative Asset Price Path", fontsize=14, fontweight='bold')
    #cahrt title
    plt.xlabel("Trading Date", fontsize=12)
    #x-axis labelling
    plt.ylabel("Price ($)", fontsize=12)
    #y-axis labelling
    plt.xticks(df['Date'][::30], rotation=45)
    # x.ticks -> Where to place {bookmarks}
    # [::30] -> every 30 days       rotation -> 45 degrees

    plt.grid(True, linestyle='--', alpha=0.5)
    #grid -> turns the chart easily read
    #linestyles -> Dashed line          alpha -> transparency
    plt.legend(loc='upper left')
    #legend -> what's the chart line means      loc -> what position?
    plt.tight_layout()
    #automatically adjusts spacing

    plt.show()
    # Display the interactive chart on your screen

except Exception as e:
    print(f"Pipeline Error: {e}")