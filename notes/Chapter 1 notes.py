def future():
    age = eval(input("enter your age: "))
    futureage = age + 20
    print('in 20 years you will be', futureage)


def convert():
    print("lets convert!")
    celsius = eval(input("what is the temp in celsius?"))
    fahrenheit = celsius * 9 / 5 + 32
    print("that temperature is", fahrenheit, "degrees fahrenheit.")


def test():
    print("hello, world!")
    print("Hello", "world!")
    print(2 + 3)
    print(2.0 + 3.0)
    print("2 + 3 =", 2 + 3)
    print(2 * 3)
    print(2 ** 3)
    print(2 / 3)
    for i in range(5):
        print(i * i)
    for d in [3, 1, 4, 1, 5]:
        print(d, end=" ")
    for i in range(4):
        print("Hello", end=" !!!")
    for i in range(7, 3, -1):
        print(i, 2 ** i)


def horsepower():
    watts = eval(input("enter the amount of watts: "))
    horse_power = watts * 745.7 / 745.7
    print("your total horse power is:", horse_power)

# chapter 5/ strings,
# strings-are sequence of character """" Ex. "hello, world!"
# list- are sequences of any object [ you initialize a list with  square brackets]
# an element is in a list that can be  any data types
# the syntax of a list is ["paul", "george", "john", "ringo"] or it can be
# a list of integers [3,1,4,1,5,9] or [ 3, "monday",4, "tuesday"]
# you can store strings and lists in variables
# there is a build in  function of python  called length
# for strings  it counts th entire  string of list for example,
# for  strings it will count the  entire  number count of said word for
# list it will count each word in the bracket in quotes
# plus operator (concatenation) to put things together
# EX. "hello" + "world" = "helloworld" or "hello + " " "world"
# if you add a string and a string to a variable the variable  will return to a string
# you can not at a string to a list  plus a operator because  the operators work in specific ways  for each type
# the multiplication operator  implies repetition
# EX. c= "hi" * 2 will print hi twice
# for L in a: will print each letter of the world in a veritcle stance
# try out some of these: for  name in b:
# print(name)
# indexing is the art of grabbing one element out of the string of list
# for string indexing is counts everything in the  quotes for a list it will
# count everything that's in brackets  and quotes as a single number
# string= hello world or 0 1 2 3 4 5 6 7 8 9 0 10 11 12
# list =  b or 0 1 2 3
# c= a[] <string> [<int>], print(c)
# d= "monday" [2], print(d)
# you can also index negative numbers for example "monday" -6 -5 -4 -3 -2 -1
# name = b[-1] will name the name ringo
# b[-1] = b[len(b)-1]
# a group of string are called substring and a  group of  lists are called sublist
# slicing is another operational term to where we can pull apart  the list and or string to pull out what we want
# <str>[<int>:<int>:<int>] with the same start stop method as range
# c = a[1:8:2] do  not  need to include the step if you are  only going up  by 1 ex. print(c)
# el,w
# you have to use colons for slicing
# if you want to go to the end you can do  a colon before to represent you want everything
# before the number  you picked or a colon after for everything  after the number you picked
# you can also do negative numbers for example [ 12:6:-1] dlrow or 12::-1]
# for slicing a list, you will always get a list return b[1:2] = b[1]

