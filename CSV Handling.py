import pandas as pd

data = [
    ['Name','Age','Salary'],
    ['Alice',25,50000],
    ['Bob',30,55000],
    ['Charlie',35,60000],
    ['Diana','',52000]
]

print('Data.csv created SUCCESSFULLY')

df = pd.read_csv('data.csv')

print("\n=== CSV Inspection ===")
print("First 3 rows:\n", df.head(3))
print("\nColumns:", list(df.columns))
print("\nMissing values:\n", df.isnull().sum())


