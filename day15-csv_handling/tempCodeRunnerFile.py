import pandas as pd

df = pd.read_csv("data.csv")
print(df)

print(df.head())   # first 5 rows
print(df.tail(10))   # last 10 rows
print(df.shape)    # rows, columns
print(df.columns) 