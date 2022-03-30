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
    while not Button.is_clicked:
        if Button.is_clicked(click_door, exit_class):
            win.close()
        if Door.is_clicked(click_door, door_class):
            if not Door.is_secret():
                Door.open("white", "open")
                Door.set_secret(True)
            elif Door.is_secret(click_door):
                Door.close("red", "Closed")
                Door.set_secret(False)
            click_door = win.getMouse()








