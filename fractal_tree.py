import turtle


def draw_tree(branch_length, t):
    if branch_length > 5:
        # 绘制主枝干
        t.forward(branch_length)
        # 右转 20 度
        t.right(20)
        # 递归绘制右侧子树
        draw_tree(branch_length - 15, t)
        # 左转 40 度
        t.left(40)
        # 递归绘制左侧子树
        draw_tree(branch_length - 15, t)
        # 右转 20 度回到原来方向
        t.right(20)
        # 退回原来的位置
        t.backward(branch_length)


# 设置画布和画笔
screen = turtle.Screen()
screen.title("分形树")
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.backward(100)
t.pendown()

# 绘制分形树
draw_tree(75, t)

# 完成绘制
screen.mainloop()
    