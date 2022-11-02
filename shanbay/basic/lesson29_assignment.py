__author__ = 'ranshen0519@icloud.com'

import turtle

turtle.shape('turtle')
turtle.color('red')
turtle.hideturtle()


def draw_polygon(n):
    for i in range(n):
        turtle.forward(20)
        turtle.right(360 / n)


draw_polygon(20)
turtle.done()
