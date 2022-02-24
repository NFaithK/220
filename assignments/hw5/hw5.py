"""
Name: <your name goes here – Faith kelley>
<ProgramName>.py

Problem: < using  lists and string to solve world problems by slicing >

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Brooke, duvall>
"""


def name_reverse():
    first_last = input("enter your first and last name here: ")
    spl_first_last = str.split(first_last)
    rever_name = spl_first_last[1]
    rever_name_s = spl_first_last[0]
    print(rever_name + "," + " " + rever_name_s)


def company_name():
    domain = input(" enter a Three part domain: ")
    domain_spl = domain.split(".")
    domain_pull = domain_spl[1]
    print(domain_pull)


def initials():
    students = eval(input("How many students in the class:"))
    for i in range(students):
        student_n = input("what is the  name of student" + " " + str(i + 1) + "?")
        student_n_spl = student_n.split()
        first = student_n_spl[0]
        last = student_n_spl[1]
        first_s = first[0:1]
        last_s = last[0:1]
        print(first_s + last_s)


def names():
    name = input("Enter  a list of names separated by comas:")
    name_spl = name.split(", ")
    slice = ""
    for i in name_spl:
        current_name = i.split()
        first = current_name[0]
        last = current_name[1]
        first_n = first[0:1]
        last_n = last[0:1]
        slice = slice + first_n + last_n + " "
    print(slice)


def thirds():
    num = eval(input("enter the number of sentences"))
    sentences = []
    for i in range(num):
        sentence = input("enter" + " " + str(i + 1) + ":")
        sentences.append(sentence)

    for i in sentences:
        temp = " "
        for j in range(0,  len(i), 3):
            temp = temp + i[j: j+1]
        print(temp)
        temp = ""

def word_average():
    sum = 0
    word = input("Enter a sentence:")
    word_spl = word.split()
    num_words = len(word_spl)
    for i in word_spl:
        sum = sum + len(i)






    print(sum/num_words)


def pig_latin():
    sentence = input(" enter the sentence to convert to pig latin")
    sent_spl = sentence.split()
    for word in sent_spl:
        print(word[1:len(sentence)] + sentence[0] + "ay", end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()

