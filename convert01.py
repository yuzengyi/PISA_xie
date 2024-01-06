import pandas as pd
# Load the provided Excel file with dummy variables
file_path = 'data_with_dummies.xlsx'
data_with_dummies = pd.read_excel(file_path)

# Convert boolean values (True/False) to integers (1/0)
data_with_dummies = data_with_dummies.astype(int)

# Export the modified data to a new Excel file
output_file_path_converted = 'data_with_dummies_converted.xlsx'
data_with_dummies.to_excel(output_file_path_converted, index=False)

print(output_file_path_converted)
