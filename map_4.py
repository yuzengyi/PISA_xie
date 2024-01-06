import pandas as pd

# Load the provided Excel file again due to execution environment reset
file_path = 'data_all.xlsx'
data_all = pd.read_excel(file_path)

# Mapping values for the specified columns
value_mapping = {
    1: 15,   # Up to 30 minutes a day
    2: 45,   # More than 30 minutes and up to 1 hour a day
    3: 90,   # More than 1 hour and up to 2 hours a day
    4: 150,  # More than 2 hours and up to 3 hours a day
    5: 210,  # More than 3 hours and up to 4 hours a day
    6: 270   # More than 4 hours a day
}

# Columns to apply the mapping
columns_to_map = ['ST296Q01JA', 'ST296Q02JA', 'ST296Q03JA', 'ST296Q04JA']

# Apply the mapping
for column in columns_to_map:
    data_all[column] = data_all[column].map(value_mapping)

# Export the modified data to a new Excel file
output_file_path = 'cleaned_data_all.xlsx'
data_all.to_excel(output_file_path, index=False)

print(output_file_path)
