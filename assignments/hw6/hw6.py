"""
Name: <your name goes here Faith Kelley>
<Strings>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def cash_converter():
    integer = eval(input("Enter an integer: "))
    print('That is {:.2f}'.format(integer))


def encode():

    message = (input("enter a message:"))
    key = eval(input("enter a key:"))
    for ch in message:
        name = (ord(ch))
        name_s= name.rstrip()



def sphere_area(radius):
    radius = float(4 * math.pi * radius ** 2)
    return radius


def sphere_volume(radius):
    radius = float(((4 / 3) * math.pi * radius ** 3))
    return radius


def sum_n(number):
    number = int((number * (number + 1)) / 2)
    return number


def sum_n_cubes(number):
    number = int((number * (number + 1) / 2) ** 2)
    return number


def encode_better():
    acc = 0
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    for i in range(len(message)):
        cypher = (ord(message[i]))
        cypher_k = cypher - 65
        key_f = (ord(key[i % len(key)])) - 65
        number = (cypher_k + key_f) % 26
        cypher_b = number + 65
        cypher_chr = (chr(cypher_b))
    print(cypher_chr + acc)

if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()

