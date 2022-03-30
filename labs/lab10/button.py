"""Name: <Faith Kelley>
<Lab 10>.py
 i am the only one doing this  project
"""

from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

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

    def color_button(self, color):
        self.shape.setFill(color)

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
