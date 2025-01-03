import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science',"ieee"])
import matplotlib.pyplot as plt
# 常见的标记有'o'（圆圈），'s'（方形），'^'（上三角），'v'（下三角），'p'（五角星），'*'（星号），'D'（菱形）
# 样本数量
x = [1, 2, 3, 4, 5]

# 不同方法的准确率（假设数据）
DCFSL = [80, 78, 75, 72, 70]
Gia_CFSL = [75, 73, 70, 68, 65]
ADFSL = [70, 68, 65, 63, 60]
MLRL_FSL = [65, 63, 60, 58, 55]
FDFSL = [60, 58, 55, 53, 50]
Ours = [80, 82, 85, 87, 90]  # 假设“Ours”在所有样本数量下的表现

plt.figure(figsize=(10, 6))
# 绘制各方法的折线图，指定不同的标记和颜色
plt.plot(x, DCFSL, marker='o', markersize=8, label='DCFSL', color='blue')
plt.plot(x, Gia_CFSL, marker='s', markersize=8, label='Gia-CFSL', color='green')
plt.plot(x, ADFSL, marker='^', markersize=8, label='ADFSL', color='red')
plt.plot(x, MLRL_FSL, marker='v', markersize=8, label='MLRL-FSL', color='cyan')
plt.plot(x, FDFSL, marker='p', markersize=8, label='FDFSL', color='magenta')
plt.plot(x, Ours, marker='*', markersize=8, label='Ours', color='black')

# 设置图表标题和轴标签
plt.title('Overall Accuracy Comparison')
plt.xlabel('Number of samples per class')
plt.ylabel('Overall Accuracy (%)')
# 设置x轴刻度
plt.xticks(x)
# 添加图例
plt.legend()
# 设置y轴范围
plt.ylim(40, 90)
# 显示网格
plt.grid(True)
# 显示图形
plt.show()