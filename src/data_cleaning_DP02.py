import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('DP02.csv')
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
df = df.drop(['total_pop_household', 'pop25'], axis=1)
print("Columns after:", df.columns)
#print(df.head())
print(df.info())

# Convert data types
numeric_column_list = ['pct_high_school', 'pct_some_college',
       'pct_associate', 'pct_bachelor', 'pct_graduate', 'pct_same_house',
       'pct_diff_house', 'pct_diff_house_us', 'pct_same_county',
       'pct_diff_county', 'pct_diffCounty_sState', 'pct_diff_state',
       'pct_abroad', 'pct_native', 'pct_foreign_born']
for numeric_column in numeric_column_list:
    df[numeric_column] = df[numeric_column].astype(float)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv('DP02_selected.csv', index=False)








