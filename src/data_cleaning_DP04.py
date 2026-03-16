import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('DP04.csv')
print(df.shape)  

# Keep only marked columns
df = df.loc[:, df.iloc[0].notnull()]
print("Number of columns:", df.shape[1])
df.columns = df.iloc[0]
df = df.drop(df.index[0])
df = df.reset_index(drop=True)
print(df.shape) 
#print(df.head())

# Select columns 
print("Columns before:", df.columns)
df = df.drop(['count_house_rent', 'count_house_owner', 
    'count_occupied_house', 'pct_owner_occupied',], axis=1)
print("Columns after:", df.columns)
print(df.dtypes) 

# Check missing values
print(df.isnull().sum())

# Convert data types
df['pct_renter_occupied'] = df['pct_renter_occupied'].astype(float)

# Replace any non-numeric values with NaN
df = df.replace({'-': np.nan, 'None': np.nan, '': np.nan})
selected_columns = ['median_house_value', 'pct_houseValue300k', 'pct_houseValue500k', 'pct_houseValue1M', 'gross_rent_median']
df[selected_columns] = df[selected_columns].apply(pd.to_numeric, errors='coerce')
print(df.dtypes)

# Save the cleaned dataset
df.to_csv('DP04_selected.csv', index=False)













