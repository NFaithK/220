"""
Faith Kelley,
lab4.py
today we are trying to find the averages of roads
I certify that I am the only  one   doing this work"""

from graphics import *


def greeting_card():
    win = GraphWin("Valentines Greeting Card", 500, 500)
    win.setBackground("pink")
    c = Circle(Point(200, 150), 100)
    c_t = Circle(Point(300, 150), 100)
    t_polygon = Polygon([Point(113, 200), Point(387, 200), Point(250, 450)])
    c.setFill("red")
    c.setOutline("red")
    c_t.setFill("red")
    c_t.setOutline("red")
    t_polygon.setFill("red")
    t_polygon.setOutline("red")
    aline = Line(Point(50, 400), Point(200, 300))
    aline.setArrow("last")
    c.draw(win)
    c_t.draw(win)
    t_polygon.draw(win)
    aline.draw(win)
    message = Text(Point(250, 175), "Happy Valentines Day!")
    message.setStyle("bold italic")
    message.draw(win)
    for i in range(10):
        aline.move(50, -50)
        time.sleep(0.15)
    message = Text(Point(250, 470), "Please click to close")
    message.draw(win)
    win.getMouse()
    win.close()


