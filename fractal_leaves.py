import numpy as np
import matplotlib.pyplot as plt
import time


def ifs(p, eq, init, n):
    """
        进行函数迭代
        p: 每个函数的选择概率列表
        eq: 迭代函数列表
        init: 迭代初始点
        n: 迭代次数

        返回值： 每次迭代所得的X坐标数组, Y坐标数组, 计算所用的函数下标    
    """

    # 迭代向量的初始化
    pos = np.ones(3, dtype=np.float32)
    pos[:2] = init

    # 通过函数概率，计算函数的选择序列
    p = np.add.accumulate(p)    
    rands = np.random.rand(n)
    select = np.ones(n, dtype=np.int32)*(n-1)
    for i, x in enumerate(p[::-1]):
        select[rands<x] = len(p)-i-1

    # 结果的初始化
    result = np.zeros((n,2), dtype=np.float32)
    c = np.zeros(n, dtype=np.float32)

    for i in range(n):
        eqidx = select[i] # 所选的函数下标
        tmp = np.dot(eq[eqidx], pos) # 进行迭代
        pos[:2] = tmp # 更新迭代向量
        # 保存结果
        result[i] = tmp
        c[i] = eqidx

    return result[:,0], result[:, 1], c


if __name__ == "__main__":

    # 蕨类植物叶子的迭代函数和其概率值
    eq1 = np.array([[0,0,0],[0,0.16,0]])
    p1 = 0.01

    eq2 = np.array([[0.2,-0.26,0],[0.23,0.22,1.6]])
    p2 = 0.07

    eq3 = np.array([[-0.15, 0.28, 0],[0.26,0.24,0.44]])
    p3 = 0.07

    eq4 = np.array([[0.85, 0.04, 0],[-0.04, 0.85, 1.6]])
    p4 = 0.85

    start = time.time()
    x, y, c = ifs([p1,p2,p3,p4],[eq1,eq2,eq3,eq4], [0,0], 100000)
    time.time() - start
    plt.figure(figsize=(6,6))
    plt.subplot(121)
    plt.scatter(x, y, s=1, c="g", marker="s", linewidths=0)
    plt.axis("equal")
    plt.axis("off")
    plt.subplot(122)
    plt.scatter(x, y, s=1,c = c, marker="s", linewidths=0)
    plt.axis("equal")
    plt.axis("off")
    plt.subplots_adjust(left=0,right=1,bottom=0,top=1,wspace=0,hspace=0)
    plt.gcf().patch.set_facecolor("#D3D3D3")
    plt.show()