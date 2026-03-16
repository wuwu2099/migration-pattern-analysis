import pandas as pd
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt 


df = pd.read_csv('combined_new.csv') 
print(df.columns)

# Target variable and factor variables
y = df['pct_diff_state']
factor_variables = df[['pct_high_school', 'pct_some_college', 'pct_associate',
       'pct_bachelor', 'pct_graduate', 'pct_foreign_born',
       'unemploy_rate', 'pct_below_poverty', 'median_house_value',
       'gross_rent_median', 'pct_renter_occupied', 'pct_houseValue300k',
       'pct_houseValue500k', 'pct_houseValue1M', 'median_age', 'pct_male',
       'pct_age2024', 'pct_age2534', 'pct_age3544', 'pct_age4554',
       'pct_age5559', 'pct_age6064', 'pct_under18', 'pct_over65']]

X = factor_variables.fillna(factor_variables.mean())  # Fill missing values with mean 


# Example with MSE (Mean Squared Error) as the scoring metric
model = LinearRegression()
rfecv = RFECV(estimator=model, step=1, cv=KFold(10), scoring='neg_mean_squared_error')

rfecv.fit(X, y)

# Get the selected features
selected_features = X.columns[rfecv.support_]

# Print results
print(f"\nTarget Variable: pct_diff_state")
print(f"Optimal number of features: {rfecv.n_features_}")
print(f"Selected predictors: {list(selected_features)}")

# Plot the number of features vs. cross-validation score
plt.figure()
plt.plot(range(1, len(rfecv.cv_results_['mean_test_score']) + 1), rfecv.cv_results_['mean_test_score'])
plt.xlabel("Number of features selected")
plt.ylabel("Cross-validation score (MSE)")
plt.title("RFECV - Feature Selection (MSE)")
plt.show()
