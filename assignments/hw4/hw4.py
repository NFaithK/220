"""
Name: <your name goes here – Faith Kelley>
<homework 4>.py

Problem: <We are using graphing to create different objects>

Certification of Authenticity:
<include one of the following>
I certify that I had someone from the CSL department help me and his name was brooke"""

from graphics import *
import math


def squares():
    win = GraphWin("Square Clicks", 500, 500)
    text_1 = Text(Point(250, 250), "Click to draw a square")
    text_1.draw(win)
    p1 = Point(150, 100)
    p2 = Point(200, 150)
    rect = Rectangle(p1, p2)
    rect.setFill("red")
    rect.setOutline("red")
    rect.draw(win)
    for i in range(5):
        p3 = win.getMouse()
        rect2 = Rectangle(Point(p3.getX() - 25, p3.getY() - 25), (Point(p3.getX() + 25, p3.getY() + 25)))
        rect2.draw(win)
        rect2.setFill("red")
        rect2.setOutline("red")
    text = Text(Point(350, 350), "click to close")
    text.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 500, 500)
    text_close = Text(Point(250, 250), "Click again to close")
    text_close.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    rect = Rectangle(p1, p2)
    rect.setFill("green")
    rect.setOutline("green")
    rect.draw(win)
    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    area = length * width
    perimeter = 2 * (length + width)
    text_perimeter = Text(Point(250, 350), "Perimeter:  " + str(perimeter))
    text_perimeter.draw(win)
    text_area = Text(Point(250, 450), "Area:  " + str(area))
    text_area.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 500, 500)
    cp1 = win.getMouse()
    cp2 = win.getMouse()
    radius = math.sqrt(((cp2.getX() - cp1.getX()) ** 2 + (cp2.getY() - cp1.getY()) ** 2))
    circ = Circle(cp1, int(radius))
    circ.setFill("orange")
    circ.setOutline("orange")
    text_r = Text(Point(250, 450), "Radius:    " + str(radius))
    text_r.draw(win)
    text_circ = Text(Point(250, 250), "Click again to close")
    text_circ.draw(win)
    circ.draw(win)
    win.getMouse()
    win.close()


def pi2():
    total = 0
    n = eval(input("Enter the number of terms to sum: "))
    numadd = int(n / 2) + (n % 2)
    numsub = int(n / 2)
    for i in range(numadd):
        num = 4
        denom = 4*i+1
        frac = num/denom
        total = total + frac
    for i in range(numsub):
        num = 4
        denom = 4 * i + 3
        frac2 = num/denom
        total = total-frac2
    approx = abs(math.pi - total)
    print("pi approximation:", total)
    print("accuracy: ", approx)