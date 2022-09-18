import turtle

turtle.reset()

count = 0
x = -300
y = 300

while (count <= 5):
    turtle.penup()
    turtle.goto(x, y-(count*100))
    turtle.pendown()
    turtle.forward(500)
    count += 1

count = 0
turtle.right(90)

while (count <= 5):
    turtle.penup()
    turtle.goto(x+(count*100), y)
    turtle.pendown()
    turtle.forward(500)
    count += 1


turtle.exitonclick()
