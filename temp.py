import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 示例数据
data = {
    'A': [0.79, 0.75, 0.8],
    'B': [1.00, 0.98, 0.79],
    'C': [0.81, 0.97, 0.89],
    'D': [0.99, 0.80, -1.00],
    'E': [1.00, 0.98, 0]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 绘制相关图
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Graph')
plt.show()

# 绘制矩阵散点图
sns.pairplot(df)
plt.suptitle('Matrix Scatterplot', y=1.02)
plt.show()