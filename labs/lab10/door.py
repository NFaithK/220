"""Faith Kelley
lab10.py
I am the only one  working on this project"""

from graphics import *


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        upper_left = self.shape.getP1()
        lower_right = self.shape.getP2()
        x_1 = upper_left.getX()
        x_2 = lower_right.getX()
        y_1 = upper_left.getY()
        y_2 = lower_right.getY()
        if x_1 <= point.getX() <= x_2:
            if y_1 <= point.getY() <= y_2:
                return True
        return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret == True:
            return True
        if self.secret == False:
            return False

    def set_secret(self, secret):
        self.secret = secret
