import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False
# 解决Matplotlib坐标轴负号'-'显示为方块的问题
sns.set(font='SimHei')
# Load the Excel file to check the column names
file_path = 'gender_grade.xlsx'
data = pd.read_excel(file_path)

# Define the columns for homework time
homework_columns = ['数学作业时间', '语言作业时间', '科学作业时间', '所有作业时间']

# Calculate the average homework time by gender
gender_means = data.groupby('性别')[homework_columns].mean()

# Calculate the average homework time by grade
grade_means = data.groupby('年级')[homework_columns].mean()

# Calculate the average homework time by teaching quality
# Replace '数学教学质量' with the correct column name for teaching quality in your dataset
teaching_quality_means = data.groupby('数学教学质量')[homework_columns].mean()

# Plotting the average homework time by gender
gender_means.plot(kind='bar', title='Average Homework Time by Gender')
plt.ylabel('Average Time (minutes)')
plt.xlabel('Gender (1: Female, 2: Male)')
plt.xticks(rotation=0)
plt.savefig('gender_homework_times.png')

# Plotting the average homework time by grade
grade_means.plot(kind='bar', title='Average Homework Time by Grade')
plt.ylabel('Average Time (minutes)')
plt.xlabel('Grade')
plt.xticks(rotation=0)
plt.savefig('grade_homework_times.png')

# Plotting the average homework time by teaching quality
teaching_quality_means.plot(kind='bar', title='Average Homework Time by Teaching Quality')
plt.ylabel('Average Time (minutes)')
plt.xlabel('Teaching Quality')
plt.xticks(rotation=0)
plt.savefig('teaching_quality_homework_times.png')

# Export the averages to an Excel file
output_file_path = 'homework_time_stats.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    gender_means.to_excel(writer, sheet_name='Gender Mean Times')
    grade_means.to_excel(writer, sheet_name='Grade Mean Times')
    teaching_quality_means.to_excel(writer, sheet_name='Teaching Quality Mean Times')

print("Analysis complete. Data exported to", output_file_path)
