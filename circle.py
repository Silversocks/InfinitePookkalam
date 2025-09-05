import turtle
import math

epsilon=0.1
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
    
def edist(x1,y1,x2,y2):
    return abs(math.sqrt((x1-x2)**2+(y1-y2)**2))

def validate(i,allcircles,a,b,c):
    for j in allcircles:
        if edist(i.x,i.y,j.x,j.y)<0.1:
            return False
    if not tangent(i,a) and not tangent(i,b) and not tangent(i,c):
        return False
    return True 

def tangent(c1,c2):
    d=c1.dist(c2)
    r1=c1.r
    r2=c2.r
    return d-(r1+r2)<epsilon or d-abs(r1-r2)<epsilon


def draw(allcircles):
    for i in allcircles:
        i.draw()