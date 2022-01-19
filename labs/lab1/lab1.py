"""
Faith Kelley,
lab1.py
today we are trying to   find monthly interest for a bill,
i certify that i am the only  one   doing this work"""


def monthly_interest():
    anual_interest = eval(input("what is your annual interest rate?:"))
    billing_cycle = eval(input("what is  the billing cycle?:"))
    previousnet_balance = eval(input("what is your previous net balance?:"))
    payment = eval(input("what did you pay?: "))
    paidday = eval(input("when did you pay your balance?: "))
    netcyle = previousnet_balance * billing_cycle
    netbalance = payment * (billing_cycle - paidday)
    subbalance = netcyle - netbalance
    avedaily = subbalance / billing_cycle
    avedailyR = round(avedaily, 2)
    monthlyinterest = avedailyR * (anual_interest / 12) / 100
    monthlyinterestR = round(monthlyinterest, 2)
    print("your netcyle is!: $", netcyle)
    print("your net balance is!: $", netbalance)
    print("your sub  balance is!: $", subbalance)
    print("your average daily balance is!: $", avedailyR)
    print("your monthly Interest is!: $", monthlyinterestR)
