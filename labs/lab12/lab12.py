"""Faith Kelley
  Lab 12.py
  I certify i am the only one that is doing this work"""
from random import randint


def find_and_remove(list, value):
    if list.count(value) != 0:
        list_v = list.index(value)
        list.insert(list_v, "Faith")
        list.pop(value)


def good_input():
    user_input = eval(input("Enter a number between 1-10 inclusive:"))
    while not 1 <= user_input <= 10:
        if 1 <= user_input <= 10:
            return user_input
        elif user_input < 1:
            user_input = eval(input(" Your input is too low!, try again! Enter a number between 1-10 inclusive:"))
        elif user_input > 10:
            user_input = eval(input(" Your input is too high!, try again! Enter a number between 1-10 inclusive:"))


def num_digits():
    user_input = 1
    count = 0
    while user_input > 0:
        user_input = eval(input("Enter number here:"))
        user_input_n = user_input
        while user_input_n != 0:
            user_input_n = user_input_n // 10
            count += 1
            print(count)


def hi_lo_game():
    acc = 0
    random_number = randint(1, 100)
    user_input = eval(input("Guess a number from 1-100"))
    right = False
    while not right:
        acc += 1
        if acc < 10:
            if user_input < random_number:
                user_input = eval(input("Thats too low, try going higher!, the range is 1-100"))
            elif user_input>random_number:
                user_input = eval(input("Thats too high!, try going lower!, the range is 1-100"))
            elif user_input == random_number:
                print("YOU ARE THE WINNER!,  tries is took{}".format(acc))
                right = True
        else:
            print("Sorry you lost!")


