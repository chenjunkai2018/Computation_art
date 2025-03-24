import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import cm

def iter_point(c):
    z = c
    for i in range(1, 100): # 最多迭代100次
        if abs(z)>2: break # 半径大于2则认为逃逸
        z = z*z+c
    return i # 返回迭代次数

def draw_mandelbrot(cx, cy, d):

    x0, x1, y0, y1 = cx-d, cx+d, cy-d, cy+d 
    y, x = np.ogrid[y0:y1:200j, x0:x1:200j]
    c = x + y*1j
    start = time.time()
    mandelbrot = np.frompyfunc(iter_point,1,1)(c).astype(np.float32)
    print("time=",time.time() - start)
    plt.imshow(mandelbrot, cmap=cm.jet, extent=[x0,x1,y0,y1])
    plt.gca().set_axis_off()

if __name__ == "__main__":

    x, y = 0.27322626, 0.595153338

    plt.subplot(231)
    draw_mandelbrot(-0.5,0,1.5)
    for i in range(2,7):    
        plt.subplot(230+i)
        draw_mandelbrot(x, y, 0.2**(i-1))

    plt.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)
    plt.show()