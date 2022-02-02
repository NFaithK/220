"""
Faith Kelley,
lab3.py
today we are trying to find the averages of roads
i certify that i am the only  one   doing this work"""


def traffic():
    total_acc = 0
    roads_surveyed = eval(input("how many roads were surveyed?"))
    for i in range(roads_surveyed):
        print("how many days was road", i + 1, "surveyed")
        days = eval(input(" "))
        travel_acc = 0
        for e in range(days):
            print("\tHow many cars traveled on day", e + 1)
            cars_traveled = eval(input(" "))
            travel_acc = travel_acc + cars_traveled
            total_acc = total_acc + cars_traveled
        road_answer = travel_acc / days
        print("Road", i + 1, "average vehicles per day", road_answer)

    print("Total number of vehicles traveled on all roads:", total_acc)
    print("Average number of vehicles per road:", total_acc / roads_surveyed)
