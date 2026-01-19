import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取 CSV
# 1. 读取数据
result_path = '../result'
benchmark_name = 'sift'
df = pd.read_csv(f"{result_path}/{benchmark_name}.csv")

horizontal_metric = 'recall'
vertical_metric = 'QPS'

# 2. 只保留需要的列（避免脏数据）
df = df[[horizontal_metric, vertical_metric]]

# 3. 转为数值类型（非常关键）
df[horizontal_metric] = pd.to_numeric(df[horizontal_metric])
df[vertical_metric] = pd.to_numeric(df[vertical_metric])
# 4. 按 Recall 升序排序
df = df.sort_values(by=horizontal_metric)

# 5. 绘图
plt.figure()
plt.plot(df[horizontal_metric], df[vertical_metric])
plt.xlabel(horizontal_metric)
plt.ylabel(vertical_metric)
plt.grid(True)
# 6. 保存图像
plt.savefig(f"{benchmark_name}.png", dpi=150)
plt.show()