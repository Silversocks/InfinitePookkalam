import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
screen.tracer(0, 0)

t.speed(0)
t.pensize(2)
t.hideturtle()


colors = ["#FF6347", "#FFD700", "#32CD32", "#FF69B4", "#1E90FF", "#DA70D6"]


def triangle(x, y, r, d=0, color="#FF1E1E"):
    l = (r*math.sqrt(3))/2

    t.color(color)
    t.fillcolor(color)
    t.penup()
    t.goto(x, y)
    t.setheading(d)
    t.forward(l / 2)
    t.left(120)     
    t.pendown()

    t.begin_fill()
    for _ in range(3):
        t.forward(l)
        t.left(120)
    t.end_fill()

def draw_circle(x,y,radius,color):
    t.penup()
    t.goto(x+radius, y)  
    t.setheading(0)  
    t.pendown()
    t.color("white")
    t.lt(90)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius=radius)
    t.end_fill()

def draw_qcircle(colors):
    t.penup()
    t.goto(0, 0)  
    t.setheading(0)  
    t.pendown()
    t.color("white")
    for i in range(4):
        t.fillcolor(colors[i])
        t.backward(75)
        t.rt(90)
        t.begin_fill()
        t.circle(75,90,200) 
        t.lt(90)
        t.forward(75)
        t.end_fill()

draw_circle(0,0,165,"light green")

for i in range(24):
    angle = 360 / 24
    triangle(0, 0, 200, i * angle,"red")
for i in range(24):
    angle=360/24
    triangle(0,0,165,i*angle+7.5,color="orange")
for i in range(24):
    angle=360/24
    triangle(0,0,130,i*angle,color="yellow")

draw_qcircle(["red","orange","green","yellow"])

screen.update()
turtle.done()
