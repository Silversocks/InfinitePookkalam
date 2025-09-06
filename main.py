import math
import turtle

epsilon=0.1 
t = turtle.Turtle(visible=False)
t.speed(10)
t.pensize(0.1)
depth=5

screen = turtle.Screen()
screen.tracer(0, 0)  # disable updae, do not delete line

class circle:
    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k
        self.r = abs(1 / k)

    def draw(self):
        t.penup()
        t.goto(self.x, self.y - self.r)
        t.pendown()
        t.circle(self.r,steps=200)
    
    def dist(self,n1):
        return math.sqrt((self.x-n1.x)**2+(self.y-n1.y)**2)

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
        circle(sumn.add(rootn).scale(1/k4[0]).a,sumn.add(rootn).scale(1/k4[0]).b,k4[0]),
        circle(sumn.sub(rootn).scale(1/k4[0]).a,sumn.sub(rootn).scale(1/k4[0]).b,k4[0]),
        ]

def edist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def validate(i,allcircles,a,b,c):
    for j in allcircles:
        if i.dist(j)<0.1:
            return False
    if not tangent(i,a) or not tangent(i,b) or not tangent(i,c):
        return False
    return True 

def tangent(c1,c2):
    d=c1.dist(c2)
    r1=c1.r
    r2=c2.r
    return abs(d-(r1+r2))<epsilon or abs(d-abs(r2-r1))<epsilon


def draw(allcircles):
    for i in allcircles:
        i.draw()

#basically doing recursion
def cycle(q,allcircles):
    nextq=[]
    for i in q:
        [a,b,c]=i
        k4=descartes(a,b,c)
        r4=abs(1/k4[0])
        newcircles=complex_decartes(a,b,c,k4)    
        for i in newcircles:
            if validate(i,allcircles,a,b,c):
                allcircles.append(i)
                t1=[a,b,i]
                t2=[c,b,i]
                t3=[a,c,i]
                nextq.append(t1)
                nextq.append(t2)
                nextq.append(t3)
    return nextq

if __name__=="__main__":
    c1=circle(100,100,-1/200)
    c2=circle(0,100,1/100)
    c3=circle(200,100,1/100)

    allcircles=[c1,c2,c3]
    q=[[c1,c2,c3]]

    k4=descartes(c1,c2,c3)
    r4=abs(1/k4[0])

    cp=complex_decartes(c1,c2,c3,k4)
    c4,c5=cp[0],cp[1]

    for i in range(depth):
        q=cycle(q,allcircles)
    draw(allcircles)

    screen.update()  # Refresh screen after drawing all circles

    turtle.done()