import turtle
import math

t = turtle.Turtle(visible=False)

class circle:
    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k
        self.r = abs(1 / k)

    def draw(self):

        t.penup()
        t.goto(self.x, self.y - self.r)  # Move to bottom of circle
        t.pendown()
        t.circle(self.r)
        turtle.hideturtle()
    
    def dist(self,n1):
        return edist(self.x,self.y,n1.x,n1.y)
    
def draw(allcircles):
    for i in allcircles:
        i.draw()

def edist(x1,y1,x2,y2):
    return abs(math.sqrt((x1-x2)**2+(y1-y2)**2))