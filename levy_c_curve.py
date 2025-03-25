import turtle
import numpy as np

def levy_c_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        t.right(45)
        levy_c_curve(t, order - 1, size / np.sqrt(2))
        t.left(90)
        levy_c_curve(t, order - 1, size / np.sqrt(2))
        t.right(45)


# 设置画布和画笔
screen = turtle.Screen()
screen.title("Levy C Curve")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pendown()

# 绘制莱维C形曲线
order = 8
size = 400
levy_c_curve(t, order, size)

# 完成绘制
screen.mainloop()
    