"""
Name: <your name goes here Faith Kelley>
<Strings>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: < brook duvall from csl>
"""
import math


def cash_converter():
    integer = eval(input("Enter an integer: ")) # we asked the user for an integer
    print('That is {:.2f}'.format(integer)) # then we formatted to come back with a   rounded number  with 2 zeros


def encode():
    acc = "" #  this is the accumulator for this function
    message = (input("enter a message:")) # we asked the  user for a message
    key = eval(input("enter a key:")) # we then asked the user for a key
    for ch in message: # we   used a for loop
        name = (ord(ch)) # we asked for the ordinal  letter in the word ( we asked the  number for each letter in the  message
        name_n = name + key # we added the  ordinal number  plus the key that was already given to us
        name_ch = chr(name_n) # we then turned this back into letters
        acc = acc + name_ch # we used an accumulator  for this  to add the  letters together back into a sentence
    print(acc) # we printed it


def sphere_area(radius):
    radius = float(4 * math.pi * radius ** 2) # we floated the equation  and then multiplied it by pi times the radius squared
    return radius # we then printed it


def sphere_volume(radius):
    radius = float(((4 / 3) * math.pi * radius ** 3)) # we floated the number but by doing this we divided it by 4/3s and multiplied by pi times radius and cubed it
    return radius


def sum_n(number):
    number = int((number * (number + 1)) / 2) # we multiplied the number  times the  original number plus 1 and  divived it by 2
    return number


def sum_n_cubes(number):
    number = int((number * (number + 1) / 2) ** 2) # we essentially did the same thing but this time we squared it after we did it
    return number


def encode_better():
    finished_t = "" #  we used a empty string
    message = input("enter the message: ") # we tol the mto enter a message that they wanted encoded
    key = input("Enter a key") # we then told them to  add a key
    for i in range(len(message)): # we are  using a for loop
        cypher = (ord(message[i])) - 65 # we are getting the  ordinal numbers of the message  and then we are subtracting by 65
        key_f = (ord(key[i % len(key)])) - 65 #  then we are  essentiall doing the same thing but this time we are using the length of the key instead and we are using modulo
        number = (cypher + key_f) % 58 # then we are  adding the cypher plus the  key together and mudelo to get a remainder
        cypher_b = number + 65 # then we are adding  65 back to our original statement
        finished = (chr(cypher_b)) # then we turn those numbers bakc into  letters
        finished_t = finished_t + finished # we are then  using the  accumulator we made  to combine those letter back into a  sentence of words
    print(finished_t)

if __name__ == '__main__':
    pass
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