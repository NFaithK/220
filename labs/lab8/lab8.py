"""Faith Kelley
Lab8.py
 today we are  creating a game
  I certify i am the only person that is  working on this project"""
import math

from random import randint

from graphics import *


def get_random(move_amount):
    move_amount = randint(-move_amount, move_amount)
    return move_amount


def did_collide(ball, ball_2):
    c_radius = ball.getRadius()
    c2_radius = ball_2.getRadius()
    c_center = ball.getCenter()
    c_ball = c_center.getX()
    c_ball2 = c_center.getY()
    c_center_2 = ball_2.getCenter()
    c2_ball = c_center_2.getX()
    c2_ball_2 = c_center_2.getY()
    distance = ((c2_ball - c_ball) * (c2_ball - c_ball)) + ((c2_ball_2 - c_ball2) * (c2_ball_2 - c_ball2))
    distance_2 = math.sqrt(distance)
    add_radius = c_radius + c2_radius
    return distance_2 <= add_radius


def hit_vertical(ball, win):
    win_top = win.getHeight()
    radius_b = ball.getRadius()
    center_b = ball.getCenter()
    y_ball = center_b.getY()
    distance_ball = radius_b + y_ball
    negative = y_ball - radius_b
    return distance_ball >= win_top or negative <= 0


def hit_horizontal(ball, win):
    win_side = win.getWidth()
    radius_b = ball.getRadius()
    center_b = ball.getCenter()
    x_ball = center_b.getX()
    distance_ball = radius_b + x_ball
    negative = x_ball - radius_b
    return negative <= 0 or distance_ball >= win_side


def get_random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    return color_rgb(r, b, g)


def bumper():
    win = GraphWin("Bumper Cars", 500, 500)
    Circle_1 = Circle(Point(randint(0, 500), randint(0, 500)), 25)
    Circle_1.setFill(get_random_color())
    Circle_1.draw(win)
    Circle_2 = Circle(Point(randint(0, 500), randint(0, 500)), 25)
    Circle_2.setFill(get_random_color())
    Circle_2.draw(win)

    move_amount = 23
    circle_1x = get_random(move_amount)
    circle_1y = get_random(move_amount)
    circle_2x = get_random(move_amount)
    circle_2y = get_random(move_amount)
    while not win.checkMouse():
        Circle_1.move(circle_1x, circle_1y)
        Circle_2.move(circle_2x, circle_2y)
        time.sleep(0.5)
        if did_collide(Circle_1, Circle_2):
            circle_1x = -circle_1x
            circle_1y = -circle_1y
            circle_2x = -circle_2x
            circle_2y = -circle_2y
            Circle_1.move(circle_1x, circle_1y)
            Circle_2.move(circle_2x, circle_2y)
        if hit_horizontal(Circle_1, win):
            circle_1x = -circle_1x
            Circle_1.move(circle_1x, circle_1y)
        if hit_horizontal(Circle_2, win):
            circle_2x = -circle_2x
            Circle_2.move(circle_2x, circle_2y)
        if hit_vertical(Circle_1, win):
            circle_1y = -circle_1y
            Circle_1.move(circle_1x, circle_1y)
        if hit_vertical(Circle_2, win):
            circle_2y = circle_2y
            Circle_2.move(circle_2x, circle_2y)
    win.close()
