import numpy as np
import matplotlib.pyplot as plt


def julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    M = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] * Z[mask] + c
        M[mask] = i

    return M


# 初始参数
c = complex(-0.7, 0.27015)
xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0
width, height = 800, 600
max_iter = 100
zoom_levels = 5
zoom_factor = 0.5

# 迭代放大
for i in range(zoom_levels):
    # 计算当前范围的中心
    center_x = (xmin + xmax) / 2
    center_y = (ymin + ymax) / 2
    # 计算新的范围
    new_width = (xmax - xmin) * zoom_factor
    new_height = (ymax - ymin) * zoom_factor
    xmin = center_x - new_width / 2
    xmax = center_x + new_width / 2
    ymin = center_y - new_height / 2
    ymax = center_y + new_height / 2

    # 计算朱利亚集
    J = julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter)

    # 绘制图像
    plt.imshow(J.T, extent=[xmin, xmax, ymin, ymax], cmap='summer', origin='lower')
    plt.colorbar()
    plt.title(f'Julia Set Zoom Level {i + 1}')
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.show()
    