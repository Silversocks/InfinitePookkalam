import math
import turtle

class circle:
    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k
        self.r = abs(1 / k)

    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y - self.r)  # Move to bottom of circle
        t.pendown()
        t.circle(self.r)

#section is to define imaginary numbers and various methods, skip if needed
class imgn:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def add(self,n2):
        return imgn(self.a+n2.a,self.b+n2.b)
    def sub(self,n2):
        return imgn(self.a-n2.a,self.b-n2.b)
    def scale(self,num):
        return imgn(self.a*num,self.b*num)
    def mult(self,n2):
        return imgn(self.a*n2.a - self.b*n2.b, self.a*n2.b + self.b*n2.a)
    def sqrt(self):
        r = math.sqrt(self.a**2 + self.b**2)
        o = math.atan2(self.b, self.a)
        r = math.sqrt(r)
        o = o / 2
        return imgn(r * math.cos(o), r * math.sin(o))


def descartes(c1,c2,c3):
    add=c1.k+c2.k+c3.k
    root=2*math.sqrt(c1.k*c2.k+c2.k*c3.k+c3.k*c1.k)
    return [add+root,add-root]

def complex_decartes(c1,c2,c3,k4):
    f1=imgn(c1.x,c1.y).scale(c1.k)
    f2=imgn(c2.x,c2.y).scale(c2.k)
    f3=imgn(c3.x,c3.y).scale(c3.k)
    sumn=f1.add(f2).add(f3)
    rootn=f1.mult(f2).add(f2.mult(f3)).add(f3.mult(f1)).sqrt().scale(2)
    return [
        circle(sumn.add(rootn).scale(1/k4[0]).a,sumn.add(rootn).scale(1/k4[0]).b),
        circle(sumn.sub(rootn).scale(1/k4[0]).a,sumn.sub(rootn).scale(1/k4[0]).b),
        circle(sumn.add(rootn).scale(1/k4[1]).a,sumn.add(rootn).scale(1/k4[1]).b),
        circle(sumn.sub(rootn).scale(1/k4[1]).a,sumn.sub(rootn).scale(1/k4[1]).b),
        ]

c1=circle(100,100,-1/200)
c2=circle(0,100,1/100)
c3=circle(200,100,1/100)
c1.draw()
c2.draw()
c3.draw()

k4=descartes(c1,c2,c3)
r4=abs(1/k4[0])

cp=complex_decartes(c1,c2,c3,k4)
c4,c5=cp[0],cp[1]
c4=circle(c4.a,c4.b,k4[0])
c5=circle(c5.a,c5.b,k4[0])
c4.draw()
c5.draw()