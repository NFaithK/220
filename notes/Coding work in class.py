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


def get_discount(price, sale):
    price = price * (1 - sale)
    return price


def names():
    name = input("Enter  a list of names separated by comas:")  # we asked the   user  to input a name  using a commas
    name_spl = name.split(", ")  # we split the word using the comma what was inputed
    slice = ""  # accumulator sort of
    for i in name_spl:
        current_name = i.split()
        first = current_name[0]
        last = current_name[1]
        first_n = first[0:1]
        last_n = last[0:1]
        slice = slice + first_n + last_n + " "
    print(slice)


def thirds():
    num = eval(input("enter the number of sentences"))
    sentences = []
    for i in range(num):
        sentence = input("enter" + " " + str(
            i + 1) + ":")  # this is reitterating the num  so it will loop as many times as it needs us too
        sentences.append(sentence)  # this is putting the words together
        for i in sentences:  # for loop
            temp = " "  # empty line
            for j in range(0, len(i), 3):  # this is taking the   word from the previous for loop and its skipping by 3
                temp = temp + i[j: j + 1]
            print(temp)


def pig_latin():
    sentence = input(" enter the sentence to convert to pig latin")  # we are asking the  the user for sentence input
    sent_spl = sentence.split()  # we are splitting  the word by spaces
    for word in sent_spl:  # for loop
        print(word[1:len(sentence)] + sentence[0] + "ay",
              end=" ")  # for the lenth of the world we only want to takout the end portion and then add
