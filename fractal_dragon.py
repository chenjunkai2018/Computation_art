import turtle


def dragon_curve(order, length, angle, direction):
    if order == 0:
        turtle.forward(length)
    else:
        if direction == 1:
            dragon_curve(order - 1, length, angle, 1)
            turtle.right(angle)
            dragon_curve(order - 1, length, angle, -1)
        else:
            dragon_curve(order - 1, length, angle, 1)
            turtle.left(angle)
            dragon_curve(order - 1, length, angle, -1)


# 设置画布和画笔
screen = turtle.Screen()
screen.title("分形龙")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, 0)
t.pendown()

# 绘制分形龙
order = 10  # 分形的阶数
length = 10  # 线段长度
angle = 90  # 转弯角度
dragon_curve(order, length, angle, 1)

# 完成绘制
screen.mainloop()
