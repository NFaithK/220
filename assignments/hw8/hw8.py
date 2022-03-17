"""
Name: <your name goes here – Faith Kelley>
<homework 8py

Problem: < we using  functions to create other   functions>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Brooke>
"""
import math

from graphics import GraphWin, Circle, Text, Point



def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]+10




def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2



def sum_list(nums):
    acc = 0
    for i in nums:
        acc = i + acc
    return acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    ret = []
    for i in range(len(nums)):
        nums_spl = nums[i].split(", ")
        to_numbers(nums_spl)
        square_each(nums_spl)
        sum = sum_list(nums_spl)
        ret.append(sum)
    return ret



def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    return False


def leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius = math.sqrt(
        (center_2.getX() - circumference_point_2.getX()) ** 2 +
        (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius)
    circle_two.setFill("red")
    circle_two.draw(win)
    over_text = Text(Point(5,5),"The circles did overlap")
    no_over = Text(Point(5,5),"The circles did not overlap")
    if did_overlap(circle_one,circle_two):
        over_text.draw(win)
    else:
        no_over.draw(win)
    close_text = Text(Point(5, 7), " click to close")
    close_text.draw(win)
    win.getMouse()
    win.close()







def did_overlap(circle_one, circle_two):
    c_radius = circle_one.getRadius()
    c2_radius = circle_two.getRadius()
    c_center = circle_one.getCenter()
    c_ball = c_center.getX()
    c_ball2 = c_center.getY()
    c_center_2 = circle_two.getCenter()
    c2_ball = c_center_2.getX()
    c2_ball_2 = c_center_2.getY()
    distance = math.sqrt(math.pow(c2_ball-c_ball, 2)+math.pow(c2_ball_2-c_ball2, 2))
    add_radius = c_radius + c2_radius
    return distance <= add_radius



if __name__ == '__main__':
    pass
