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
    win = GraphWin("Surprise Door game", 1000, 1000)
    exit_button = Rectangle(Point(50, 50), Point(100, 100))
    exit_class = Button(exit_button, "Exit!")
    exit_class.draw(win)

    door_graph = Rectangle(Point(100, 150), Point(300, 600))
    door_class_1 = Door(door_graph, "Door 1")
    door_class_1.color_door("SaddleBrown")
    door_class_1.draw(win)
    door_graph = Rectangle(Point(350, 150), Point(550, 600))
    door_class_2 = Door(door_graph, "Door 2")
    door_class_2.color_door("SaddleBrown")
    door_class_2.draw(win)
    door_graph = Rectangle(Point(600, 150), Point(800, 600))
    door_class_3 = Door(door_graph, "Door 3")
    door_class_3.color_door("SaddleBrown")
    door_class_3.draw(win)

    score_board = Rectangle(Point(800, 100), Point(900, 150))
    wins_box = score_board.getCenter()
    wins_number = Text(wins_box, "0")
    score_board_2 = Rectangle(Point(900, 100), Point(1000, 150))
    losses_box = score_board_2.getCenter()
    losses_number = Text(losses_box, "0")
    score_board.draw(win)
    score_board_2.draw(win)
    wins_number.draw(win)
    losses_number.draw(win)
    words = Text(Point(500, 100), " There is a secret door!")
    words.draw(win)
    any_click = Text(Point(500, 150), "Click to play the game!")
    any_click.draw(win)
    wins_box = Text(Point(850, 138), "Wins")
    wins_box.draw(win)
    click_anywhere_1 = Text(Point(970, 138), "Losses")
    click_anywhere_1.draw(win)
    wins = 0
    losses = 0
    game_end = False
    user_click = win.getMouse()
    secret_door = door_class_1.is_secret
    while not game_end:
        if exit_class.is_clicked(user_click):
            game_end = True
            win.close()
        if secret_door.is_clicked(user_click):
            secret_door.color_door("green")
            non_secret_door.color_door("red")
            words.undraw()
            message = Text(Point(500, 200), "you win!")
            message.draw(win)
            new = Text(Point(500, 300), "Click to play Again!")
            new.draw(win)
            wins += 1
            any_click.undraw()
            win_f = Text(wins_box, "{}".format(wins))
            win_f.draw(win)
            reset = win.getMouse()
            if exit_class.is_clicked(reset):
                game_end = True
                win.close()
            else:
                door = randint(1, 3)
                if door == 1:
                    door_class_1.set_secret(True)
                    secret_door = door_class_1
                elif door == 2:
                    door_class_2.set_secret(True)
                    secret_door = door_class_2
                else:
                    door_class_3.set_secret(True)
                    secret_door = door_class_3
                door_class_1.color_door("SaddleBrown")
                door_class_2.color_door("SaddleBrown")
                door_class_3.color_door("SaddleBrown")
                new.undraw()
                message.undraw()
                any_click.draw(win)
                words.draw(win)
        else:
            if door_class_1.is_clicked(user_click):
                non_secret_door = door_class_1
            elif door_class_2.is_clicked(user_click):
                non_secret_door = door_class_2
            else:
                non_secret_door = door_class_2
                secret_door.color_door("green")
                non_secret_door.color_door("red")
                words.undraw()
                message_1 = Text(Point(500, 200), "Sorry! that was incorrect!")
                message_1.draw(win)
                message_1.draw(win)
                new = Text(Point(500, 800), "Click to play Again!")
                new.draw(win)
                wins += 1
                any_click.undraw()
                losses_f = Text(wins_box, "{}".format(losses))
                losses_f.draw(win)
                reset = win.getMouse()
                new.draw(win)
                if exit_class.is_clicked(reset):
                    game_end = True
                    win.close()
                else:
                    door = randint(1, 3)
                    if door == 1:
                        door_class_1.set_secret(True)
                        secret_door = door_class_1
                    elif door == 2:
                        door_class_2.set_secret(True)
                        secret_door = door_class_2
                    else:
                        door_class_3.set_secret(True)
                        secret_door = door_class_3
                        door_class_1.color_door("SaddleBrown")
                        door_class_2.color_door("SaddleBrown")
                        door_class_3.color_door("SaddleBrown")
                        new.undraw()
                        message_1.undraw()
                        any_click.draw(win)
                        words.draw(win)





