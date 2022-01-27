"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem
 that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    multiple_sum = 0
    upper_bound = eval(input("what is your upper bound: "))
    for i in range(upper_bound):
        multiple_sum = (upper_bound + multiple_sum)
    print(multiple_sum)


print()


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end='\t')

    print('')


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("enter side b length: "))
    side_c = eval(input("enter side c length: "))
    side_s = side_a + side_b + side_c
    side_s = side_s / 2
    area_s1 = side_s - side_a
    area_s2 = side_s - side_b
    area_s3 = side_s - side_c
    area_t = side_s * area_s1 * area_s2 * area_s3
    area_t = math.sqrt(area_t)
    print(area_t)


def sum_squares():
    lower_range = eval(input("enter your lower range:"))
    upper_range = eval(input("enter your upper range:"))
    range_r = list(range(lower_range, upper_range + 1))

    print(range_e)


def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("enter exponent: "))
    answer = base ** exponent
    print(base, "^", exponent, "=", answer)


if __name__ == '__main__':
    pass
