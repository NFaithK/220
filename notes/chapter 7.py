import math

# control structures  ( for loops, functions)
# decision structures (allows program to execute different statements depending on some condition



def convert():
    print("lets convert!")
    celsius = eval(input("what is the temp in celsius?"))
    fahrenheit = celsius * 9 / 5 + 32
    print("that temperature is", fahrenheit, "degrees fahrenheit.")

    # if <condition>:
    # <body>
    # condition is an expression, this is called a relational operators
    # less than <
    # less than or equal <=
    #  greater than >
    # greater than or equal to >=
    # equality ==
    # not equal !=
    # bool-boolean
    # boolean mathmatics have true and false

    # if 7 > 3:


def quadratic(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        print('no real roots')
    elif disc == 0:
        # you can also use elif which actually needs a condition just like
        # the plain if it can also be on the same chain
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        print('double root at:', root_1)
    else:
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        root_2 = (-b - sqrt_discr) / denom
        print(root_1, root_2)

    # bool and bool will return a boolean
    # Ex. x > 3  and x < 10
    def faith(a,b,c):
        if a >= b and a >= c:
            return a
        if b >= a and b >= c:
            return b
        if c >= a and c >= b:
            return
    # another option
    # if a >= b
    # if a>=c:
    # else return c

    def hehe( a, b , c):
         max_value = a
          if b > max_value:
              max_value = b
          if c > max_value:
              max_value = c
#def max(values)
#max_value values[0]
# for value in values
# if value >= max_value:
# max_value = value
# return value return value
# return max( insert items here ) would also work




