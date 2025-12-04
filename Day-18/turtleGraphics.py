import turtle as t
import random

#create turtle object
turtle = t.Turtle()
turtle.shape('turtle')
screen = t.Screen()
screen.colormode(255)

# turtle.fd(100)

# Generate random color

def generate_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


random_color = generate_color()
# Todo: 1 Draw a square

# for _ in range(4):
#     turtle.rt(360 /4)
#     turtle.fd(100)


# Todo: 2 Draw a dashed line

# position turtle at the start
turtle.penup()
turtle.goto(-200,200)

for _ in range(10):
    turtle.pendown()
    turtle.fd(20)
    turtle.penup()
    turtle.fd(20)


# turtle.clear()
# turtle.reset()










screen.exitonclick()