import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Define the columns for homework time
homework_columns = ['数学作业时间', '语言作业时间', '科学作业时间', '所有作业时间']
plt.rcParams['font.sans-serif'] = ['SimSun']
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False
# 解决Matplotlib坐标轴负号'-'显示为方块的问题
sns.set(font='SimSun')
# Load the Excel file
file_path = 'gender_grade.xlsx'
data_education = pd.read_excel(file_path)

# Define the mapping for parental education levels
education_mapping = {
    6: '初级教育',
    9: '较初级教育',
    12: '中等教育',
    14.5: '较高等教育',
    16: '高等教育'
}

# Map the '父母最高教育指数' column to the corresponding education levels
data_education['父母最高教育水平'] = data_education['父母最高教育指数'].map(education_mapping)

# Calculate the average homework time for each education level
education_level_means = data_education.groupby('父母最高教育水平')[homework_columns].mean()

# Reorder the index based on the education level sequence
education_order = ['初级教育', '较初级教育', '中等教育', '较高等教育', '高等教育']
education_level_means = education_level_means.reindex(education_order)

# Plotting the average homework time by parental education level
education_level_means.plot(kind='bar', title='Average Homework Time by Parental Education Level')
plt.ylabel('Average Time (minutes)')
plt.xlabel('Parental Education Level')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('education_level_homework_times_ordered.png')

# Export the averages to an Excel file
output_file_path_education = 'education_level_homework_stats_ordered.xlsx'
education_level_means.to_excel(output_file_path_education)


print(education_level_means, output_file_path_education)
