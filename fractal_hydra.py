import turtle

def hydra_tree(t, order, length, branches):
    if order == 0:
        t.forward(length)
    else:
        for _ in range(branches):
            t.forward(length)
            t.left(360 / branches)
            hydra_tree(t, order - 1, length * 0.6, branches)
            t.right(360 / branches)
            t.backward(length)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.left(90)
hydra_tree(t, order=3, length=100, branches=3)
screen.mainloop()