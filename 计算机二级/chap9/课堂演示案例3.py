import turtle as t
#t.forward(100)
#t.forward(-200)

#t.backward(100)
t.backward(-100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(-100)
t.goto(0,0)

t.setx(-200)
t.sety(-200)

t.setheading(120)
t.forward(100)

t.home()
t.penup()
t.goto(100,100)
t.pendown()
t.circle(50)


t.penup()

t.goto(200,200)
t.pendown()
t.circle(50,90)

t.penup()
t.goto(220,220)
t.pendown()
t.dot(20,'red')
