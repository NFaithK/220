"""Faith Kelley
Lab10.py
I am the only one doing this  project"""
from graphics import *
from button import Button
from door import Door


def main():
    win = GraphWin("Surprise Door", 500, 500)
    exit_button = Rectangle(Point(50, 50), Point(450, 150))
    exit_class = Button(exit_button, "Exit!")
    exit_class.draw(win)

    door_graph = Rectangle(Point(100, 150), Point(350, 450))
    door_class = Door(door_graph, "Closed")
    door_class.color_door("red")
    door_class.draw(win)

    click_door = win.getMouse()
    while not exit_class.is_clicked:
        if exit_class.is_clicked(click_door):
            win.close()
        if door_class.is_clicked(click_door):
            if not door_class.is_secret():
                door_class.open("white", "open")
                door_class.set_secret(True)
            elif door_class.is_secret():
                door_class.close("red", "Closed")
                door_class.set_secret(False)
            click_door = win.getMouse()
