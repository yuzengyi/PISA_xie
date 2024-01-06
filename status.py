import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the provided Excel file
file_path = 'gender_grade.xlsx'
data = pd.read_excel(file_path)

# Define the columns for homework time
homework_columns = ['数学作业时间', '语言作业时间', '科学作业时间', '所有作业时间']

# Set the font for plots
plt.rcParams['font.sans-serif'] = ['SimHei']  # Set font to SimHei to display Chinese characters
plt.rcParams['axes.unicode_minus'] = False    # Fix for minus sign display issues
sns.set(font='SimHei')                        # Set seaborn font to SimHei

# Create scatter plots for each homework column against the economic, social, and cultural status index
for column in homework_columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='经济社会文化地位指数', y=column, data=data)
    plt.title(f'Scatter Plot of {column} vs. 经济社会文化地位指数')
    plt.xlabel('经济社会文化地位指数')
    plt.ylabel(column)
    plt.savefig(f'{column}_scatter_plot.png')

# Output file paths for the scatter plots
output_files_scatter = [f'{column}_scatter_plot.png' for column in homework_columns]
print(output_files_scatter)
