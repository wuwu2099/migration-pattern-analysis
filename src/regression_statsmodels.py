import statsmodels.api as sm
import pandas as pd
import numpy as np

df = pd.read_csv('combined_new.csv') 
#print(df.columns)

# Assuming df is already loaded
y = df['pct_diff_state']
factor_variables = df[['pct_high_school', 'pct_some_college', 'pct_associate',
                       'pct_bachelor', 'pct_graduate', 'pct_foreign_born',
                       'unemploy_rate', 'pct_below_poverty', 'median_house_value',
                       'gross_rent_median', 'pct_houseValue300k',
                       'pct_houseValue500k', 'pct_houseValue1M', 'median_age', 'pct_male',
                       'pct_age2024', 'pct_age2534', 'pct_age3544', 'pct_age4554',
                       'pct_age5559', 'pct_under18', 'pct_over65']]

# Handle missing values by replacing them with the column mean
factor_variables = factor_variables.fillna(factor_variables.mean())

# Handle infinite values by replacing them with large values
factor_variables.replace([np.inf, -np.inf], np.nan, inplace=True)
factor_variables.fillna(factor_variables.mean(), inplace=True)  # Refill after replacing Inf with NaN

# Add constant to factor_variables for intercept
X = sm.add_constant(factor_variables)

# Forward selection process
remaining_features = list(X.columns)  # List all feature columns
remaining_features.remove('const')  # Remove the constant from the list of features
best_features = []  # Features selected for the model
current_score, best_new_score = float('inf'), float('inf')  # Initial scores for comparison

# Start with no variables in the model
while remaining_features:
    scores_with_candidates = []
    for feature in remaining_features:
        # Build the model with the current best features and the candidate feature
        model = sm.OLS(y, X[best_features + [feature]]).fit()
        aic = model.aic  # Use AIC as the criterion for model selection
        scores_with_candidates.append((aic, feature))  # Store AIC and feature name
    
    # Sort the candidates based on AIC, choosing the one with the lowest AIC
    scores_with_candidates.sort()
    best_new_score, best_candidate = scores_with_candidates[0]
    
    # If adding this feature improves the model (lower AIC), add it to the list
    if current_score > best_new_score:
        best_features.append(best_candidate)
        current_score = best_new_score
        remaining_features.remove(best_candidate)
        print(f"Adding feature: {best_candidate}, AIC: {best_new_score}")
        print(f"Current selected features: {best_features}")
    else:
        break  # Stop if adding new features no longer improves the model

# Final model with selected features
final_model = sm.OLS(y, X[best_features]).fit()

# Print model summary
print("\nFinal model summary:")
print(final_model.summary())

# Save model summary to a text file
with open('model_summary.txt', 'w') as f:
    f.write(final_model.summary().as_text())

