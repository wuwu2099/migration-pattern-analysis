import pandas as pd
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt 
import seaborn as sns 


# Remove duplicate columns
def remove_column(files):
    for file in files:
        df = pd.read_csv(file) 
        df = df.drop(columns=['census_tract'])
        df.to_csv(f"new_{file}", index=False)


# Merge files
def merge_files (files):
    df_list = [pd.read_csv(file) for file in files]
    merge_key = 'geo_id'  

    for i, df in enumerate(df_list):
        if merge_key not in df.columns:
            print(f"Warning: '{merge_key}' not found in file {files[i]}")

    df_merged = reduce(lambda left, right: pd.merge(left, right, on=merge_key, how='inner'), df_list)

    print(f"Merged DataFrame shape: {df_merged.shape}")
    df_merged.to_csv('combined_DP.csv', index=False)
    return df_merged


# Calculate and plot the lower triangle of the correlation matrix as a heatmap
def plot_corr_heatmap(df):
    corr_matrix = df.corr()
    # Plot heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
    plt.title('Correlation Heatmap')
    plt.show()

    plt.savefig('correlation_heatmap.png', bbox_inches='tight')  # Save as PNG
    plt.close()


if __name__ == "__main__":

    # Remove duplicate column before merging
    files = ['DP02_selected.csv', 'DP03_selected.csv', 'DP04_selected.csv', 'DP05_selected.csv']  
    remove_column(files)

    # Merge files
    files = ['new_DP02_selected.csv', 'new_DP03_selected.csv', 'new_DP04_selected.csv', 'new_DP05_selected.csv']  
    df_merged = merge_files(files)
    #print(df_merged.info())
    

    # EDA
    df_merged.set_index('geo_id', inplace=True)
    #print(df_merged.info())

    def drop_or_create_variables(df_merged):
        df_merged = df_merged.drop(columns=['pct_same_house','pct_diff_house_us','pct_same_county','pct_diff_county','pct_diff_house', 'pct_diffCounty_sState','pct_abroad'])

        #df_merged['pct_more_high_school'] = df_merged['pct_some_college'] + df_merged['pct_associate'] + df_merged['pct_bachelor'] + df_merged['pct_graduate']
        #df_merged = df_merged.drop(columns = ['pct_high_school', 'pct_some_college', 'pct_associate', 'pct_bachelor',
        #'pct_graduate'])

        df_merged['gross_rent_median'] = df_merged['gross_rent_median'] / 100
        df_merged['median_house_value'] = df_merged['median_house_value'] / 100000

        print(df_merged['median_house_value'].head())
        
        df_merged.drop('pct_native', axis=1, inplace=True)  
        return df_merged   
    
    df_merged = drop_or_create_variables(df_merged)
    print(df_merged.columns)

    def reOrder_reName_columns(df_merged):
        df_merged = df_merged[['pct_diff_state', 'pct_diffCounty_sState', 
       'pct_foreign_born', 'unemploy_rate', 'pct_below_poverty',
       'gross_rent_median', 'median_age', 
       'pct_under18', 'pct_over65', 'pct_more_high_school','pct_male']]
        
        new_column_names = ['diff_state', 'diff_County', 'foreign', 'unemploy', 
            'poverty', 'rent', 'age', 'under18', 'over65', 'more_high_school','male']
        
        df_merged.columns = new_column_names 
        print(df_merged.columns)
        #plot_corr_heatmap(df_merged)
        return df_merged 

    #df_merged = reOrder_reName_columns(df_merged)
    # Save the data with re-named columns

    # df_merged.to_csv('combined and renamed.csv', index=True)
    df_merged.to_csv('combined_new.csv', index=True)


    plot_corr_heatmap(df_merged)

    # Assuming 'y' is the dependent variable and 'X' contains independent variables
    # Here, we will use seaborn to plot the relationship between y and each indicator in X
    y = df_merged['pct_diff_state']
    X = df_merged[['pct_high_school', 'pct_some_college', 'pct_associate',
       'pct_bachelor', 'pct_graduate', 'pct_foreign_born',
       'unemploy_rate', 'pct_below_poverty', 'median_house_value',
       'gross_rent_median', 'pct_renter_occupied', 'pct_houseValue300k',
       'pct_houseValue500k', 'pct_houseValue1M', 'median_age', 'pct_male',
       'pct_age2024', 'pct_age2534', 'pct_age3544', 'pct_age4554',
       'pct_age5559', 'pct_age6064', 'pct_under18', 'pct_over65']]





    