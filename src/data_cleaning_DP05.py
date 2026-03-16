import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('DP05.csv')
print(df.shape)  

# Keep only marked columns
df = df.loc[:, df.iloc[0].notnull()]
print("Number of columns:", df.shape[1])
df.columns = df.iloc[0]
df = df.drop(df.index[0])
df = df.reset_index(drop=True)
print(df.shape) 

# Select columns 
print("Columns before:", df.columns)
df = df.drop(['pop_male', 'pop_female', 'pop_65years', 'pct_female'], axis=1)
print("Columns after:", df.columns)
print(df.dtypes) 
print(df.head())

# Check missing values
print(df.isnull().sum())

# Convert data types
num_col_list = ['median_age', 'pct_male', 'pct_under18', 'pct_age2024',
       'pct_age2534', 'pct_age3544', 'pct_age4554', 'pct_age5559',
       'pct_age6064', 'pct_under18', 'pct_over65']
for num_col in num_col_list:
    df[num_col] = df[num_col].astype(float)

print(df.dtypes)


# Save the cleaned dataset
df.to_csv('DP05_selected.csv', index=False)













