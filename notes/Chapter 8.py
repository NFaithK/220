# Chapter 8 booleans


# def is_equal(p1,p2):
# if p1.getX() == p2.getX() and p1.getY() == p2.getY():
# return True
# return False


def is_game_over(player_one_points, player_two_points):
    if player_one_points >= 15 or player_two_points >= 15 >= 2:
        won_by_two = abs(player_one_points, player_two_points)
       return True
    player_one = 0
    player_two = 0
    print(player_one, player_two)
    while not is_game_over(player_one, player_two):
        one, two = eval(input('enter score for player one and two: '))
        player_one = player_one + one
        player_two = player_two + one
    print("GAME OVER")
    #  x is equal to and, + is equal to or, 0 is equal to  false , 1 is equal to  true

def deMorgan_one(a,b):
    return not(a and b) == (not a or not b)


def deMorgan_test():
    test = [[True, True], [True, False], [False, True], [False, False]]
    for test in test:
        a = test[0]
        b = test[1]
        result = deMorgan_one(a, b)
        print('input: {},output: {}' .format(test , result))

    # truthy/ falsy
    # if score
