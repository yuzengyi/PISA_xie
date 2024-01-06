import pandas as pd

# Load the provided Excel file
file_path = 'furtherdata.xlsx'  # Replace with your actual file path
data = pd.read_excel(file_path)

# List of categorical variables
categorical_vars = ['ST001D01T', 'ST004D01T', 'ST272Q01JA', 'MISCED', 'FISCED', 'HISCED']

# Convert categorical variables to dummy variables (0 and 1)
data_dummies = pd.get_dummies(data, columns=categorical_vars, drop_first=True)

# Export the modified data to a new Excel file
output_file_path = 'data_with_dummies_01.xlsx'  # Replace with your desired output path
data_dummies.to_excel(output_file_path, index=False)

print("Data with dummy variables saved to", output_file_path)
