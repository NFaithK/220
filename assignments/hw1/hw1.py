"""
Name: <Faith Kelley>
<ProgramName>.py

Problem: < The problem we are solving would  be  common ways,  by using formulas for this coding assignment you will
be able to  get the correct amounts >

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
" I certify this is my own work"""


def calc_rec_area():
    length = eval(input("enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("enter the length:"))
    width = eval(input("enter the width:"))
    height = eval(input("enter the height:"))
    volume = length * width * height
    print("Volume=", volume)


def shooting_percentage():
    shots = eval(input("enter how many  total shots: "))
    made = eval(input("enter how many shots the player made: "))
    shootingpercentage = made / shots * 100
    print("shooting percentage= ", shootingpercentage,"%")


def coffee():
    pounds = eval(input("enter how many pounds of  coffee would  you like: "))
    totalcost = 10.50 * pounds + 0.86 * pounds + 1.50
    print("your total is: ", totalcost)


def kilometers_to_miles():
    kilo = eval(input("how many kilometers did you travel?: "))
    miles = kilo * 0.621371
    print("thats", miles, "miles!")


if __name__ == '__main__':
    pass
