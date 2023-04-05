import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

x = np.arange(-2, 2, 0.01)

y = 2*np.sin(np.pi*x)*np.sin(np.pi*x/2) / (np.pi * np.pi * x *x)

plt.title("一元二次函数")
plt.plot(x, y)
plt.show()
