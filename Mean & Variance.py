print(' ----- Pure Python Mean & Variance -----')
def mean(data):
    return sum(data) / len(data) if data else None

def variance(data):
    n = len(data)
    if n < 2:
        return None
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (n - 1)

number=[25,30,35,40,42]

print('Mean: ',mean(number))
print('Variance: ',variance(number))

print('\n---- Pandas Version Mean & Variance ----')
import pandas as pd
series = pd.Series(number)
print("\nPandas mean:", series.mean())
print("Pandas var:", series.var())

# Apply to a numeric column (e.g., age) ignoring missing values
df =pd.read_csv('data.csv')
ages = df['age'].dropna().tolist()   # convert to list, remove NaN
if ages:
    print("\n=== Statistics (pure Python) ===")
    print(f"Mean age: {mean(ages):.2f}")
    print(f"Variance of age: {variance(ages):.2f}")