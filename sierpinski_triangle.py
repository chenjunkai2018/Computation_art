import turtle


def sierpinski(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order - 1, size / 2)
        t.forward(size / 2)
        sierpinski(t, order - 1, size / 2)
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)
        sierpinski(t, order - 1, size / 2)
        t.left(60)
        t.backward(size / 2)
        t.right(60)


# 设置画布和画笔
screen = turtle.Screen()
screen.title("谢尔宾斯基三角形")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -100)
t.pendown()

# 绘制谢尔宾斯基三角形
sierpinski(t, order=4, size=400)

# 完成绘制
screen.mainloop()