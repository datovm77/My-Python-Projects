import numpy as np
import matplotlib.pyplot as plt

# ================= 修复部分开始 =================
# 1. 设置字体为 SimHei (黑体)，这是 Windows 系统自带的通用中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 2. 解决保存图像是负号 '-' 显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
# ================= 修复部分结束 =================

# 设置绘图风格 (注意：某些风格可能会覆盖字体设置，所以字体设置要在 style 之后或者再次确认，
# 为了保险，我们这里暂时不用 style，直接用默认加 grid)
# plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(10, 6), dpi=100)
plt.grid(True, linestyle='--', alpha=0.6) # 手动开启网格

# 1. 定义函数 f(x) = 0.5 * x^2 + 1
def f(x):
    return 0.5 * x**2 + 1

# 2. 定义导数（切线斜率） f'(x) = x
def df(x):
    return x

# 3. 设定切点 x0 和 目标点 x
x0 = 2
target_x = 3  # 我们想估算 x=3 时的值

y0 = f(x0)
slope = df(x0)

# 4. 生成曲线数据
x_vals = np.linspace(0.5, 4, 100)
y_vals = f(x_vals)

# 5. 生成切线数据 (线性近似公式)
def tangent_line(x):
    return y0 + slope * (x - x0)

y_tangent = tangent_line(x_vals)

# --- 开始绘图 ---

# 画曲线 f(x)
plt.plot(x_vals, y_vals, label='真实曲线 $y = f(x)$', color='blue', linewidth=2)

# 画切线 (线性近似)
plt.plot(x_vals, y_tangent, label='切线近似 $y = L(x)$', color='red', linestyle='--', linewidth=2)

# 标记切点 A (x0, f(x0))
plt.scatter([x0], [y0], color='black', zorder=5)
plt.text(x0 - 0.2, y0 + 0.5, '切点 $A(x_0, f(x_0))$', fontsize=12, fontweight='bold')

# 标记目标点 B (在曲线上) 和 近似点 C (在切线上)
true_val = f(target_x)
approx_val = tangent_line(target_x)

plt.scatter([target_x], [true_val], color='blue', zorder=5)
plt.text(target_x + 0.1, true_val, '真实值 $f(x)$', fontsize=12, color='blue')

plt.scatter([target_x], [approx_val], color='red', zorder=5)
plt.text(target_x + 0.1, approx_val - 0.5, '近似值 (公式结果)', fontsize=12, color='red')

# 画辅助线三角形
plt.plot([x0, target_x], [y0, y0], 'k:', linewidth=1) # 水平线 dx
plt.plot([target_x, target_x], [y0, approx_val], 'k:', linewidth=1) # 垂直线 dy

# 标注 dx 和 dy (注意这里加了 r 前缀，修复 invalid escape sequence 警告)
plt.text((x0 + target_x)/2, y0 - 0.4, r'$\Delta x = x - x_0$', fontsize=10, ha='center')
plt.text(target_x + 0.1, (y0 + approx_val)/2, r'增量 = $f\'(x_0)(x-x_0)$', fontsize=10, ha='left')

# 填充误差区域
plt.vlines(target_x, approx_val, true_val, color='green', alpha=0.5, linewidth=3, label='误差')

plt.title('线性近似几何解释图', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.xlim(0.5, 4.5)
plt.ylim(0, 10)

plt.show()