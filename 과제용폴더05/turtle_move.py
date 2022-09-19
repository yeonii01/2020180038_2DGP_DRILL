import turtle

def right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def down():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(right,'d')
turtle.onkey(left,'a')
turtle.onkey(up,'w')
turtle.onkey(down,'s')
turtle.onkey(restart,'Escape')
turtle.listen()
