"""
Name: <your name goes here – Faith Kelley>
<homework 3>.py

Problem: <we are using loops to figure out real world problems>

Certification of Authenticity:
<include one of the following>
I certify that i had someone from the CSL department help me and his name was brooke"""


def average():
    grade_acc = 0
    many_grades = eval(input("how many grades will you enter?"))
    for _ in range(many_grades):
        grades = eval(input("Enter grade:"))
        grade_acc = grades + grade_acc
    grade_average = grade_acc / many_grades
    print("Average is:", grade_average)


def tip_jar():
    donate_acc = 0
    for _ in range(5):
        donate = eval(input("how much would you like to donate? "))
        donate_acc = donate + donate_acc
    total_don = donate_acc
    print("Total tips:", total_don)


def newton():
    square_root = eval(input("What number do you want to square root? "))
    times = eval(input("How many times should we improve the approximation?"))
    approx = square_root
    for i in range(times):
        approx = float(approx + (float(square_root) / float(approx))) / float(2)
    print("the square root is approximately", approx)


def sequence():
    terms = eval(input("how many terms would you like?"))
    for i in range(-1, terms - 1):
        print(i + (i % 2) + 1)


def pi():
    product = 1
    terms = eval(input("How many terms in  the series? "))
    for i in range(0, terms):
        num = ((i - 1) % 2) + i + 1
        den = i + (i % 2) + 1
        product = product * float(num) / float(den)
    print(num ** 2)

if __name__ == '__main__':
    pass
