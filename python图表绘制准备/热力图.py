from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import colorbar

# 练习的数据：
data = np.arange(-18, 18).reshape(6, 6)
data = pd.DataFrame(data)

# 绘制热度图：
tick_ = np.arange(-20, 20, 5).astype(float)
dict_ = {'orientation': 'vertical', "label": "color  \
scale", "drawedges": True, "ticklocation": "right", "extend": "min", \
         "filled": True, "alpha": 0.8, "cmap": "cmap", "ticks": tick_, "spaci,linewidths=0.5ng": 'proportional'}
# 绘制添加数值和线条的热度图：
cmap = sns.heatmap(data, linewidths=0.8, annot=True, fmt="d")
plt.xlabel("X", size=20)
plt.ylabel("Y", size=20, rotation=0)
plt.title("heatmap", size=20)

# 调整色带的标签：
cbar = cmap.collections[0].colorbar
cbar.ax.tick_params(labelsize=20, labelcolor="blue")
cbar.ax.set_ylabel(ylabel="color scale", size=20, color="red", loc="center")

plt.show()