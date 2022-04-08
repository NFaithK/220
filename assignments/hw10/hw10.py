def fibonacci(n):
    add = [0, 1]
    if n < 1:
        return None
    else:
        while len(add) <= n:
            add.append(add[-1] + add[-2])
        return add[-1]


def double_investment(principal, rate):
    total = principal * 2
    principal = principal
    year = 0
    while principal < total:
        principal *= (1 + rate)
        year += 1
    return year


def syracuse(number):
    add = []
    add.append(number)
    while number != 1:
        if number % 2 != 0:
            number = 3 * number + 1
            add.append(number)
        else:
            number = number / 2
            add.append(number)
    return add


def goldbach(n):
    prime = range(1, n)
    print (prime)

    add = []
    if n % 2 != 0:
        return add
