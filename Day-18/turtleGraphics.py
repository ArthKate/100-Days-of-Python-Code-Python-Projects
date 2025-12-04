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
#turtle.penup()
#turtle.goto(-200,200)
#turtle.clear()
turtle.pensize(10)

# for _ in range(10):
#     turtle.pendown()
#     turtle.fd(20)
#     turtle.penup()
#     turtle.fd(20)

# Todo: 3 Draw different shapes

sides_and_colors = {
    3: 'red',
    4: 'green',
    6: 'blue',
    7: 'yellow',
    8: 'gray',
    9: 'pink',
    10: 'violet',
}

# for sides, color in sides_and_colors.items():
#     turtle.color(color)
#     for _ in range(sides):
#         turtle.fd(100)
#         turtle.rt(360 / sides)

# Todo: 4 Random walk

import random
angle_direction = [turtle.rt, turtle.lt]

for _ in range(200):
    clr = generate_color()
    turtle.pencolor(clr)
    turn = random.choice(angle_direction)
    turtle.fd(15)
    turn(90)
    turtle.fd(15)



# turtle.clear()
# turtle.reset()










screen.exitonclick()