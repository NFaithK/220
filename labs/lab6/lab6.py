"""
Faith Kelley,
lab6.py
today we are trying create a  window that  computes a  vijenere cypher
I certify that I am the only  one   doing this work"""

from graphics import *


def vigenere():
    acc = ""
    win = GraphWin("Vigenere cypher", 700, 700)
    message = Entry(Point(300, 150), 15)
    message.setTextColor("black")
    message_t = Text(Point(300, 100), "Enter your Sentence below")
    message_t.setStyle("bold")
    message.draw(win)
    message_t.draw(win)
    key = Entry(Point(300, 250), 15)
    key.setTextColor("black")
    key_t = Text(Point(300, 200), "Enter your Key below")
    key_t.setStyle("bold")
    key.draw(win)
    key_t.draw(win)
    message_text = message.getText()
    key_text = key.getText()
    for i in range(len(message_text)):
        cypher = (ord(message_text[i]))
        cypher_k = cypher - 65
        key_f = (ord(key_text[i % len(key_text)])) - 65
        number = (cypher_k + key_f) % 26
        cypher_b = number + 65
        cypher_chr = (chr(cypher_b)) + acc
        cypher_ = cypher_chr
    message = Text(Point(300, 500), "Click to close")
    rectangle_2 = Rectangle(Point(300, 400), Point(400, 300))
    button_t = Text(Point(350, 350), "Cypher!")
    cypher_message = Text(Point(300, 550), "Your Cypher is!:"+(cypher_))
    cypher_message.draw(win)
    rectangle_2.draw(win)
    button_t.draw(win)
    message.draw(win)
    win.getMouse()
    win.close()
