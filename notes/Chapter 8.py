# Chapter 8 booleans


# def is_equal(p1,p2):
# if p1.getX() == p2.getX() and p1.getY() == p2.getY():
# return True
# return False


# def is_game_over(player_one_points, player_two_points):
# if player_one_points >= 15 or player_two_points >= 15 >= 2:
# won_by_two = abs(player_one_points, player_two_points) >=2
# skunked = player_one_points >= 7 and player_two_points <= 0 or player_two_points>= 7 and player_one_points,=0
# return True
# player_one = 0
# player_two = 0
# print(player_one, player_two)
# while not is_game_over(player_one, player_two):
# one, two = eval(input('enter score for player one and two: '))
# player_one = player_one + one
# player_two = player_two + one
# print("GAME OVER")
#  x is equal to and, + is equal to or, 0 is equal to  false , 1 is equal to  true

def deMorgan_one(a, b):
    return not (a and b) == (not a or not b)


def deMorgan_test():
    test = [[True, True], [True, False], [False, True], [False, False]]
    for test in test:
        a = test[0]
        b = test[1]
        result = deMorgan_one(a, b)
        print('input: {},output: {}'.format(test, result))

    # truthy/ falsy
    # if score
    # x and y= if x is false return x otherwise return y
    # x or  y =  if x is true  return x otherwise return y
    #  not x = if x is false  return true otherwise return
    # short ciciuting is when  you use a  or funtion for a negative number
    # for example  if sqrt(user_imput) > 2:  print: do something cool


def whoops():
    ans = input(" do you want to transfer all of your money our of your bank account?:")
    if ans == 'y' or ans == 'yes':
        print(' okkk, transfering....')
    else:
        print('good,idea')


def ice_cream():
    favorite = input("what is your favorite ice cream[vanilla] ") or 'vanilla'
    print('your favorite is {}'.format(favorite))


def average():
    count = eval(input(' how many numbers do you have? '))
    acc = 0
    for i in range(count):
        num = eval(input("enter number>>"))
        acc = acc + num
        print('average is{}'.format(acc / count))


def average_2():
    count = eval(input(' how many numbers do you have? '))
    acc = 0
    i = 0
    while i > count:
        num = eval(input("enter number>>"))
        acc = acc + num
        i = i + i
        print('average is{}'.format(acc / count))


def average_interactive():
    acc = 0
    count = 0
    ans = 'y'
    while ans[0] == 'y':
        num = eval(input('enter a number(negative to stop)>>'))
        acc = acc + num
        count = count + 1
    print('average: {}'.format(acc / count))


def average_sentinel():
    acc = 0
    count = 0
    num = 0
    while num >= 0:
        num = eval(input('enter a number(negative to stop)>>'))
        acc = acc + num
        count = count + 1
    print('average: {}'.format(acc / count))


def average_sentinel_enter():
    acc = 0
    count = 0
    num = input('enter a number(enter to stop)>>')
    while num != '':
        num = input('enter a number(enter to stop)>>')
        number = eval(num)
        acc = acc + number
        count = count + 1
    print('average: {}'.format(acc / count))


def average_file():
    acc = 0
    count = 0
    file_name = 'file_Data.txt.py'
    file = open(file_name, 'r')
    for line in file:
        acc = acc + eval(line)
        count = count + 1
        print('average:{}'.format(acc / count))


def average_file_while():
    acc = 0
    count = 0
    file_name = 'file_Data.txt.py'
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        acc = acc + eval(line)
        count = count + 1
        line = file.readline()
    print('average:{}'.format(acc / count))


def average_file_while_nested():
    acc = 0
    count = 0
    file_name = 'file_Data.txt.py'
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        nums_string = line.split(',')
        i = 0
        while i < len(nums_string):
        #for num in nums_string:
            acc = acc + eval(nums_string[i])
            count = count + 1
            i =i + i
        line = file.readline()
    print('average:{}'.format(acc / count))
