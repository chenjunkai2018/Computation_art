import numpy as np
import matplotlib.pyplot as plt


def burning_ship(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = (abs(z.real) + 1j * abs(z.imag)) ** 2 + c
        n = n + 1
    return n


# 设置参数
width, height = 800, 600
xmin, xmax = -2.0, 1.0
ymin, ymax = -2.5, 0.5
max_iter = 100

# 创建网格
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

# 计算燃烧船分形
M = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        M[i, j] = burning_ship(C[i, j], max_iter)

# 绘制图像
plt.imshow(M.T, extent=[xmin, xmax, ymin, ymax], cmap='summer', origin='lower')
plt.colorbar()
plt.title('Burning Ship Fractal')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
    