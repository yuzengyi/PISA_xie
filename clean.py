import pandas as pd

# Load the Excel file
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()
print(data.head())
# Define the columns to exclude from the filtering process
exclude_columns = ['MATH', 'READ', 'SCIE']

# Get all other column names
other_columns = [col for col in data.columns if col not in exclude_columns]

# Remove rows where any of the other columns contain null, 99, or 97
data = data[~data[other_columns].isin([None, 99, 97]).any(axis=1)]

# Export the cleaned data to a new Excel file
output_file_path = 'cleaned_data.xlsx'
data.to_excel(output_file_path, index=False)

print(f"Data cleaned and exported to {output_file_path}")