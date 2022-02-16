"""Faith Kelley
Lab 5.py
We are using our skills to solve various problems that were given to us"""
from graphics import *
import math


def triangle():
    win = GraphWin("Triangle", 500, 500)
    text = Text(Point(250, 250), "click three times to create a triangle")
    text.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    tri = Polygon(p1, p2, p3)
    tri.draw(win)
    length = abs(p2.getX() - p1.getX() + (p3.getX() - p2.getX()) + (p3.getX() - p1.getX()))
    width = abs(p2.getY() - p1.getY()) + (p3.getY() - p2.getY()) + (p3.getY() - p1.getY())
    area = length / 2
    area= math.sqrt()
    area_message = Text(Point(250, 350), "area: " + str(area))
    area_message.draw(win)
    peri = 2 * (length + width)
    perimeter_message = Text(Point(250, 450), "perimeter: " + str(peri))
    perimeter_message.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 600
    win_height = 600
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 3, win_height - 30), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 60), 50)
    shape.setOutline("black")
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 60, win_height / 2 + 70)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("enter a string:")
    first = string[0]
    last = string[1]
    char_positions = string[1:4]
    con_let = first + last
    three_cha = string[0:3] * 10
    string_len = len(string)
    print(first)
    print(last)
    print(char_positions)
    print(con_let)
    print(three_cha)
    print(string)
    print(string_len)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    con_list = str(values[1] + values[3])
    num_add = values[0] + values[2]
    word_mul = str(values[1]) * 5
    list_1 = [values[2], values[3], [pt]]
    list_2 = [values[2], values[3], values[0]]
    list_3 = [values[2], values[0], float(values[5])]
    num_add_two = values[0] + values[2] + float(values[5])
    list_len = len(values)
    print(con_list)
    print(num_add)
    print(word_mul)
    print(list_1)
    print(list_2)
    print(list_3)
    print(num_add_two)
    print(list_len)


def another_series():
    pass


def target():
    pass
