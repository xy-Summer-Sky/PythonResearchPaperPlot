import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from colormaps import parula
import matplotlib as mpl
mpl.rcParams["font.family"] = "Times New Roman"
mpl.rcParams["axes.labelsize"] = 15
mpl.rcParams["xtick.labelsize"] = 12
mpl.rcParams["ytick.labelsize"] = 12
mpl.rcParams["figure.titlesize"] = 15
mpl.rcParams["axes.titlesize"] = 14

input_file_path=r".\散点图样例数据2.xlsx"
out_put_pdf='.\气泡图绘制示例_a.pdf'
out_put_png='.\气泡图绘制示例_a.png'

bubble_data = pd.read_excel(input_file_path, sheet_name="data03")

x = bubble_data.x
y = bubble_data.y
values = bubble_data["values"]
values02 = bubble_data["values02"]

fig,ax = plt.subplots(figsize=(4.2,3.5),dpi=100,facecolor="w")
pubble = ax.scatter(x=x,y=y,s=values*20,c=values02,ec="k",lw=.5,cmap = parula,vmin=min(values02),
                     vmax=max(values02))
#ax.grid(False)
#添加图例
# 设置图例参数
kw = dict(prop="sizes",  # 图例属性为尺寸
          num=5,         # 图例中显示的项目数
          color="k",     # 图例标记的颜色 k为黑色
          mec="k",       # 图例标记的边框颜色
          fmt="{x:.0f}", # 图例标记的格式
          func=lambda s: s/20)  # 图例标记的转换函数 参数为s

# 添加图例
legend = ax.legend(*pubble.legend_elements(**kw),
                    loc="upper right",  # 图例位置
                    bbox_to_anchor=(1.28, 1.),  # 图例的锚点位置
                    title="Values",  # 图例标题
                    fontsize=10,  # 图例字体大小
                    title_fontsize=11,  # 图例标题字体大小
                    handletextpad=.1,  # 图例标记与文本的间距
                    frameon=False)  # 是否绘制图例边框

# 添加颜色条
#`ax.inset_axes([1.1, 0.01, 0.08, 0.4])` 中的四个参数定义了插入轴（颜色条）的位置和大小。具体来说：

# 1. `1.1`：插入轴左边缘相对于主轴左边缘的水平位置，单位是主轴宽度的倍数。
# 2. `0.01`：插入轴下边缘相对于主轴下边缘的垂直位置，单位是主轴高度的倍数。
# 3. `0.08`：插入轴的宽度，单位是主轴宽度的倍数。
# 4. `0.4`：插入轴的高度，单位是主轴高度的倍数。

cax = ax.inset_axes([1.1, 0.01, 0.08, 0.4],  # 颜色条的插入位置和大小
                    transform=ax.transAxes)  # 使用轴坐标系

# 创建颜色条
cbar = fig.colorbar(pubble, cax=cax)
cbar.ax.set_title("Values 02", fontsize=11, pad=5)  # 设置颜色条标题及其属性
cbar.ax.tick_params(left=True, direction="in", width=.5, labelsize=10)  # 设置颜色条刻度参数
cbar.ax.tick_params(which="minor", right=False)  # 设置次刻度参数
cbar.outline.set_linewidth(.5)  # 设置颜色条边框宽度

ax.set(xlim=(10, 40),ylim=(0, 45),
       xticks=np.arange(5, 50, step=5),yticks=np.arange(0, 50, step=5),
       xlabel="X Axis Title",ylabel="T Axis Title")

fig.tight_layout()
fig.savefig(out_put_pdf,bbox_inches='tight')
fig.savefig(out_put_png,
            bbox_inches='tight',dpi=300)
plt.show()