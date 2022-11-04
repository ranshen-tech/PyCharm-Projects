__author__ = 'ranshen0519@icloud.com'
import turtle
from random import randint


def draw_star():
    turtle.color('blue')
    turtle.hideturtle()
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(10)
        turtle.right(144)
    turtle.end_fill()


# 将 ??? 改成你想画的星星个数
for i in range(99):
    turtle.speed(0)
    turtle.penup()
    x = randint(-150, 150)
    y = randint(-100, 100)
    turtle.goto(x, y)
    turtle.pendown()
    draw_star()

turtle.penup()
turtle.goto(0, -130)
turtle.pendown()
turtle.write('一闪一闪亮晶晶', font=('SimHei', 12, 'bold'))
turtle.done()

