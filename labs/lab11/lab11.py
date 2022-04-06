"""
Faith Kelley
Lab 11 3 door
 we are  creating secret door game
I  certify i am doing this alone
"""
from labs.lab10.button import Button
from labs.lab10.door import Door
from graphics import *
from random import randint


def secret_doors():
    win = GraphWin("Surprise Door", 1000, 1000)
    exit_button = Rectangle(Point(50, 50), Point(100, 100))
    exit_class = Button(exit_button, "Exit!")
    exit_class.draw(win)

    door_graph = Rectangle(Point(100, 150), Point(300, 600))
    door_class_1 = Door(door_graph, "Door 1")
    door_class_1.color_door("brown")
    door_class_1.draw(win)
    door_graph = Rectangle(Point(350, 150), Point(550, 600))
    door_class_2 = Door(door_graph, "Door 2")
    door_class_2.color_door("brown")
    door_class_2.draw(win)
    door_graph = Rectangle(Point(600, 150), Point(800, 600))
    door_class_3 = Door(door_graph, "Door 3")
    door_class_3.color_door("brown")
    door_class_3.draw(win)

    score_board = Rectangle(Point(800, 100), Point(900, 150))
    score_board_2 = Rectangle(Point(900, 100), Point(1000, 150))
    score_board.draw(win)
    score_board_2.draw(win)

    click_anywhere = Text(Point(850, 138), "Wins")
    click_anywhere.draw(win)
    click_anywhere_1 = Text(Point(970, 138), "Losses")
    click_anywhere_1.draw(win)



    click_door = win.getMouse()
    while not exit_class.is_clicked(click_door):
        door = randint(1, 3)
        if door == 1:
            door_class_1.is_secret(True)
        elif door == 2:
            door_class_2.is_secret(True)
        else:
            door_class_3.is_secret(True)

        if exit_class.is_clicked(click_door):
            click_door = win.getMouse()
