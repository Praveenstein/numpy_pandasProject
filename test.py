import pandas as pd

df = pd.read_csv("input/timeseries_q7.csv", header=0, index_col=0)
print(df.head())
print("\n\n")
index_df = pd.to_datetime(df.index)
df.index = index_df
daily_df = df.resample('M').sum()
print(daily_df.head())
