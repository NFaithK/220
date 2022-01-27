"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: < this homework is to help use be able to use arithmetic in
look forms and to figure out formula>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: brooke from CSL tutoring center>
"""
import math


def sum_of_threes():
    multiple_sum = 0
    upper_bound = eval(input("what is your upper bound: "))
    for i in range(1, int(upper_bound/3)+1):
        multiple_sum += 3 * i

    print("sum of threes is", multiple_sum)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end='\t')

        print()


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
    sum_squ = 0
    lower_range = eval(input("Enter  lower range: "))
    upper_range = eval(input("Enter upper range: "))
    for i in range(lower_range, upper_range+1):
        sum_squ = (i * i) + sum_squ
    print(sum_squ)


def power():
    expo_product = 1
    base = eval(input("Enter base:"))
    exponent = eval(input("enter exponent: "))
    for i in range(exponent):
        expo_product = base * expo_product
    print(base, "^", exponent, "=", expo_product)


if __name__ == '__main__':
    pass
