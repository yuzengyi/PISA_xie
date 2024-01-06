import pandas as pd
# Load the modified Excel file
file_path = 'cleaned_data_all.xlsx'
data_modified = pd.read_excel(file_path)

# Mapping values for the new specified columns
value_mapping_new = {
    1: 0,    # No time at all
    2: 30,   # Less than 1 hour a day
    3: 120,  # Between 1 and 3 hours a day
    4: 240,  # More than 3 hours and up to 5 hours a day
    5: 360,  # More than 5 hours and up to 7 hours a day
    6: 480   # More than 7 hours a day
}

# New columns to apply the mapping
new_columns_to_map = [
    'IC177Q01JA', 'IC177Q02JA', 'IC177Q03JA', 'IC177Q04JA',
    'IC177Q05JA', 'IC177Q06JA', 'IC177Q07JA', 'IC178Q01JA',
    'IC178Q02JA', 'IC178Q03JA', 'IC178Q04JA', 'IC178Q05JA',
    'IC178Q06JA', 'IC178Q07JA'
]

# Apply the mapping to the new columns
for column in new_columns_to_map:
    data_modified[column] = data_modified[column].map(value_mapping_new)

# Export the further modified data to a new Excel file
output_file_path_new = 'further_cleaned_data.xlsx'
data_modified.to_excel(output_file_path_new, index=False)

print(output_file_path_new)
