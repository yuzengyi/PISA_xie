## 多元线性回归分析代码

以下是用于执行多元线性回归分析的Python代码。这段代码由谢晨和虞增艺完成。

```python
import pandas as pd
import statsmodels.api as sm

# Load the data
file_path = 'data_finalModel3.xlsx'  # 替换为您的文件路径
data = pd.read_excel(file_path)

# 定义自变量
independent_vars = [
    # 列出自变量的名称
    'ST059Q01TA', 'ST059Q02JA', 'ST296Q01JA', 'ST296Q02JA', 'ST296Q03JA', 'ST296Q04JA',
    # ... 还有其他自变量 ...
]

# 定义因变量
dependent_var = 'MATH'

# 执行多元线性回归
X = data[independent_vars]
X = sm.add_constant(X)  # 添加常数项（截距）
y = data[dependent_var]
model = sm.OLS(y, X).fit()

# 获取结果摘要
summary = model.summary()

# 导出结果到Excel
output_file_path = 'linear_regression_results.xlsx'
summary.to_excel(output_file_path)

print("Linear regression results saved to", output_file_path)
