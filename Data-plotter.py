import pandas as pd
import os #a system to check & open a file
import numpy as np

file_name = "mock_market_data.csv"

if not os.path.exists(file_name):
    print("-> Yahoo Finance download bypassed. Generating local data structure...")
    date_range = pd.date_range(start="17-05-2025", periods=365, freq="D") #in period 365   /    frequency of Daily/Month/Year

    # 2. Set up the random simulation parameters
    np.random.seed(42)
    # Keeps the random numbers the same every time you run it
    #Without a seed: If you run the code again to find the bug, the prices change, the crash disappears, and you can't fix your code.

    #With a seed: The exact same sequence of prices generates every single time, letting you pause, inspect your variables, and fix your code reliably.
    starting_price = 60000

    # Generate random daily percentage changes (returns) between -2% and +2%
    daily_returns = np.random.uniform(-0.02, 0.02, 365)
                    #random -> random data #uniform -> only between -2% and 2 %

    # Accumulate the returns to create a realistic price path (Random Walk)
    # This multiplies the compounding changes sequentially
    price_path = starting_price * np.cumprod(1 + daily_returns)
    #cumprod = comulate product and join them chronologically
    percentage_returns = daily_returns * 100

    # 3. Derive Open, High, Low, Close relative to that random price path
    open_prices = price_path
    # Close is the open price plus/minus another small random intraday move
    close_prices = open_prices * (1 + np.random.uniform(-0.01, 0.01, 365))

    # Choosing maximum prices between open_prices & close_prices
    #make sure the high must be ideally >= chose prices by putting +
    high_prices = np.maximum(open_prices, close_prices) * (1 + np.random.uniform(0, 0.015, 365))
    # Choosing minimum prices between open_prices & close_prices
    # make sure the low must be ideally <= chose prices by putting -
    low_prices = np.minimum(open_prices, close_prices) * (1 - np.random.uniform(0, 0.015, 365))

    # randint (low,high)  = random integer between these numbers
    # np.random.uniform = random decimals between the numbers
    #
    random_volume = np.random.randint(3000000000, 4000000000, 365, dtype=np.int64)

    # 4. Put it all into the DataFrame
    mock_data = pd.DataFrame({
        'Date': date_range.strftime('%d-%m-%Y'),
        'Open': open_prices,
        'High': high_prices,
        'Low': low_prices,
        'Close': close_prices,
        'Volume': random_volume,
        'Daily Return (%)': percentage_returns
    })

    # Rounding prices to 2 decimal places to look like real stock prices
    mock_data = mock_data.round({'Open': 2, 'High': 2, 'Low': 2, 'Close': 2,'Daily Return (%)': 2})

    mock_data.to_csv(file_name, index=False)
    #pandas automatically set data 0,1,2 one-by-one ascending your datas
    #index= False --> blocking Pandas from turning 0,1,2 as a new column of data by addressing it as a topic
    print(f"-> successfully created local file: '{file_name}'")
try:
    # Read and print the data matrix
    df = pd.read_csv(file_name) #according to file_name....

    print("\n=========================================")
    print("    MARKET PIPELINE INITIALIZED SUCCESS  ")
    print("=========================================")
    print(f"Total Trading Days Processed: {df.shape[0]}")
    #ensure the number of rows of your data (counting the items) [no. of data]
    print(f"Data Schema Columns:          {list(df.columns)}")
    #df.columns -> reading the columns' headers     list -> cleanliness and readability

    print("\n--- Most Recent 5 Days of Data (Tail Frame) ---")
    print(df[['Date', 'Close', 'Volume']].head(5))
    #determine you're printing the first / end (head / tail) of the data

except Exception as e:
    print(f"Pipeline Error: {e}")