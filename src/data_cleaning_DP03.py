import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('DP03.csv')
print(df.shape)  

# Keep only marked columns
df = df.loc[:, df.iloc[0].notnull()]
print("Number of columns:", df.shape[1])
df.columns = df.iloc[0]
df = df.drop(df.index[0])
df = df.reset_index(drop=True)
print(df.shape) 
print(df.head())

# Select columns 
print("Columns before:", df.columns)
df = df.drop(['pop16'], axis=1)
print("Columns after:", df.columns)
print(df.head())
print(df.info())

# Convert data types
numeric_column_list = ['unemploy_rate', 'pct_below_poverty']
for numeric_column in numeric_column_list:
    df[numeric_column] = df[numeric_column].astype(float)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv('DP03_selected.csv', index=False)













