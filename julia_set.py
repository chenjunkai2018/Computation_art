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


# 设置参数
c = complex(-0.7, 0.27015)
xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0
width, height = 800, 600
max_iter = 100

# 计算朱利亚集
J = julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter)

# 绘制图像
plt.imshow(J.T, extent=[xmin, xmax, ymin, ymax], cmap='summer', origin='lower')
plt.colorbar()
plt.title('Julia Set')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()