import numpy as np
import matplotlib.pyplot as plt

def midpoint_displacement(x1, y1, x2, y2, roughness, depth):
    if depth == 0:
        return [(x1, y1), (x2, y2)]
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2 + np.random.uniform(-1, 1) * (x2 - x1) ** roughness
    left = midpoint_displacement(x1, y1, mid_x, mid_y, roughness, depth - 1)
    right = midpoint_displacement(mid_x, mid_y, x2, y2, roughness, depth - 1)
    return left[:-1] + right

x1, y1 = 0, 0
x2, y2 = 100, 0
roughness = 0.7
depth = 5
points = midpoint_displacement(x1, y1, x2, y2, roughness, depth)
x, y = zip(*points)
plt.plot(x, y)
plt.show()