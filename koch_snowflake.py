import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


# 设置画布和画笔
screen = turtle.Screen()
screen.title("科赫雪花")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 100)
t.pendown()

# 绘制科赫雪花
koch_snowflake(t, order=3, size=400)

# 完成绘制
screen.mainloop()