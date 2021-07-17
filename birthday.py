import turtle
import random
import time

# sets background
bg = turtle.Screen()
bg.bgcolor("black")
# Bottom Line 1
turtle.penup()
turtle.goto(-170, -180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160, -150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150, -120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-100, -100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-90, 0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60, 0)
turtle.color("white")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30, 0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0, 0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30, 0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

# Decoration
colors = ["red", "orange", "black", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40, -50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

time.sleep(2)
turtle.clear()
turtle.bgpic("<your image name>.gif")
time.sleep(3)
turtle.clear()
bg.bgcolor("black")


# Happy Birthday message
turtle.clear()
turtle.penup()
turtle.goto(-150, 50)
turtle.color("red")
turtle.pendown()
turtle.write("Happy Birthday <birthday boy/girl name>!!", move=False, align="center", font=("Arial", 40, "normal"))
time.sleep(5)
turtle.clear()
turtle.write("May God bless You!!", move=False, align="center", font=("Arial", 40, "normal"))
time.sleep(5)
turtle.color("black")
