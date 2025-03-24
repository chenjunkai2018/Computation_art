from vpython import *


def menger_sponge(level, size, position):
    if level == 0:
        box(pos=position, size=vector(size, size, size))
    else:
        new_size = size / 3
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if abs(i) + abs(j) + abs(k) > 1:
                        new_position = position + vector(i * new_size, j * new_size, k * new_size)
                        menger_sponge(level - 1, new_size, new_position)


# 设置场景
scene.title = "Menger Sponge"
scene.width = 800
scene.height = 600

# 绘制门格海绵
level = 2  # 迭代级别
size = 3  # 初始大小
position = vector(0, 0, 0)  # 初始位置
menger_sponge(level, size, position)
    