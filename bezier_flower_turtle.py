import turtle
import math


def bezier_point(t, p0, p1, p2, p3):
    """
    计算三次贝塞尔曲线上在参数 t 处的点
    :param t: 参数，取值范围 [0, 1]
    :param p0: 起始点
    :param p1: 第一个控制点
    :param p2: 第二个控制点
    :param p3: 结束点
    :return: 贝塞尔曲线上 t 处的点
    """
    u = 1 - t
    tt = t * t
    uu = u * u
    uuu = uu * u
    ttt = tt * t
    x = uuu * p0[0] + 3 * uu * t * p1[0] + 3 * u * tt * p2[0] + ttt * p3[0]
    y = uuu * p0[1] + 3 * uu * t * p1[1] + 3 * u * tt * p2[1] + ttt * p3[1]
    return x, y


def draw_bezier_curve(t, p0, p1, p2, p3):
    """
    绘制三次贝塞尔曲线
    :param t: turtle 对象
    :param p0: 起始点
    :param p1: 第一个控制点
    :param p2: 第二个控制点
    :param p3: 结束点
    """
    t.penup()
    t.goto(p0)
    t.pendown()
    t.hideturtle() 
    t.color('red', 'pink')
    steps = 50
    for i in range(steps + 1):
        t_val = i / steps
        point = bezier_point(t_val, p0, p1, p2, p3)
        t.goto(point)


def draw_flower(t, num_petals, radius, init_theta = 30):
    """
    绘制由贝塞尔曲线组成的花朵
    :param t: turtle 对象
    :param num_petals: 花瓣数量
    :param radius: 花朵半径
    """
    angle = 360 / num_petals
    
    for ii in range(num_petals):
        if ii == 0:
            p1_theta = init_theta
            p2_theta = -init_theta
        else:
            p1_theta = init_theta + angle * ii
            p2_theta = -init_theta + angle * ii
        
        p0 = (0, 0)
        p1 = (radius * math.cos(math.radians(p1_theta)), radius * math.sin(math.radians(p1_theta)))
        p2 = (radius * math.cos(math.radians(p2_theta)), radius * math.sin(math.radians(p2_theta)))
        p3 = (0, 0)

        draw_bezier_curve(t, p0, p1, p2, p3)
        t.left(angle)


# 设置画布和画笔
screen = turtle.Screen()
screen.title("贝塞尔曲线花朵")
t = turtle.Turtle()
t.speed(0)

# 绘制花朵
draw_flower(t, num_petals=16, radius=300, init_theta=30)

# 完成绘制
screen.mainloop()