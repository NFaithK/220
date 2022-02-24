import math

from graphics import *


def happy(holiday):
    print("happy {} to you".format(holiday))


def sing(name, holiday):
    happy(holiday)
    happy(holiday)
    print("happy {} to you {}".format(holiday, name))
    happy(holiday)


def square(num):
    x = num * num * num
    return x


three_squared = square(3)
print(three_squared)


def distance(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return d

 my_distance = distance(Point(2,3), Point(3,4))
print(my_distance)

 def get_discount(price, sale):
      price = price *(1-sale)
      return price