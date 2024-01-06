import pandas as pd
import statsmodels.api as sm

# Load the provided Excel file
file_path = 'data_final.xlsx'
data_final = pd.read_excel(file_path)

# Define the independent variables (predictors) and the dependent variable
independent_vars = ['ST059Q01TA', 'ST059Q02JA', 'ST296Q01JA', 'ST296Q02JA', 'ST296Q03JA', 'ST296Q04JA']
dependent_var = 'MATH'

# Selecting the independent and dependent variables from the dataset
X = data_final[independent_vars]
y = data_final[dependent_var]

# Adding a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Get the summary of the regression
model_summary = model.summary()

# Extract the required information: coefficients, R-squared, number of observations (N), and F-statistic
coefficients = model.params
standard_errors = model.bse
t_values = model.tvalues
p_values = model.pvalues
r_squared = model.rsquared
n = model.nobs
f_statistic = model.f_pvalue

# Creating a dataframe for the extracted information
regression_results = pd.DataFrame({
    'Coefficients': coefficients,
    'Standard Errors': standard_errors,
    't-values': t_values,
    'p-values': p_values
})
regression_results.loc['R-squared'] = [r_squared, None, None, None]
regression_results.loc['N'] = [n, None, None, None]
regression_results.loc['F-statistic'] = [f_statistic, None, None, None]

# Export the regression results to a new Excel file
output_file_path_regression = 'regression_results1.xlsx'
regression_results.to_excel(output_file_path_regression)

print(output_file_path_regression, model_summary)