import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

np.random.seed(42)
days=7
date_range = pd.date_range(start="17/05/2025", periods=days, freq='D')
file_name='wencoin_data.csv'

if not os.path.exists(file_name):
    print('Generating the local data structure....')


    daily_returns=np.random.normal(0.0008, 0.02, days)
    open_prices=np.zeros(days)
    open_prices[0]=100.00
    percentage_return= (np.exp(daily_returns) -1) *100
    close_prices=100 * np.exp(np.cumsum(daily_returns))
    # prefer theorical close (ignore infraday as noises)
    open_prices[1:]=close_prices[:-1]

    high_prices=np.maximum(open_prices,close_prices) * (1+ np.abs(np.random.normal(0,0.01,days)))
    low_prices=np.minimum(open_prices,close_prices) * (1-np.abs(np.random.normal(0,0.01,days)))
    volume=np.random.randint(300000000,400000000,days,dtype=np.int64)

    data_excel =pd.DataFrame({
        'Date': date_range.strftime('%d-%m-%Y'),
        'Open': np.round(open_prices, 2),
        'High': np.round(high_prices, 2),
        'Low': np.round(low_prices, 2),
        'Close': np.round(close_prices, 2),
        'Volume': volume,
        'Percentage Return (%)': np.round(percentage_return, 2)
    })

    data_excel.to_csv(file_name,index=False)
    print(f"Data saved to {file_name} successfully! \n")

else:
    print('File already exists, loading data..... \n')

try:

    df = pd.read_csv(file_name)
    print(f'Printing first {days} rows of data...\n')
    print(df.head(days))

    print("\nLaunching Matplotlib price chart window...\n")
    mpl.figure(figsize=(12,6))
    mpl.plot(df['Date'],df['Close'],label= 'Assest Closing Price', color='royalblue',linewidth='2')
    mpl.title('Wencoin Price Chart Window',fontsize=12,fontweight='bold')
    mpl.xlabel('Date')
    mpl.ylabel('Closing Price ($)')
    mpl.xticks(df['Date'],rotation=45)
    mpl.grid(True,linestyle='--',alpha=0.5)
    mpl.legend(loc='upper left')
    mpl.tight_layout()
    mpl.show()

    print('\nThanks for using ☜(ﾟヮﾟ☜)')

except Exception as e:
    print(f"Pipeline error: {e}")