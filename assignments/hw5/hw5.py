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
    spl_first_last = str.split(first_last) # we spilt the first and last name
    rever_name = spl_first_last[1] # we got the index of  the  newly split word  of the last word
    rever_name_s = spl_first_last[0]  # we go the  index of the first word
    print(rever_name + "," + " " + rever_name_s) # we put it together using concatenation


def company_name():
    domain = input(" enter a Three part domain: ") # we asked the  user for 3 part url
    domain_spl = domain.split(".") # we split them by the  periods
    domain_pull = domain_spl[1] # we  index the name of the word
    print(domain_pull) # we pulled the  index of one which would of been the  name of the website


def initials():
    students = eval(input("How many students in the class:")) # we asked what  the amount of  students in the class
    for i in range(students): # for loop
        student_n = input("what is the  name of student" + " " + str(i + 1) + "?")
        student_n_spl = student_n.split() # we split the name of the student
        first = student_n_spl[0] # we indexed the first and the last name which this would be the first name
        last = student_n_spl[1] # this would be the last name
        first_s = first[0:1] # after we indexed it we  sliced it to get the first last of each portion of the name
        last_s = last[0:1] # we sliced the last name also and we got the first letter of it
        print(first_s + last_s) #  printed the  first  letter of  the  first name and last name of the  word


def names():
    name = input("Enter  a list of names separated by comas:") # we asked the   user  to input a name  using a commas
    name_spl = name.split(", ") # we split the word using the comma what was inputed
    slice = "" # accumulator sort of
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
    sum = 0 # this is a accumulator
    word = input("Enter a sentence:") #   we are telling the user to enter a sentence
    word_spl = word.split() # we are splitting the words by the spaces
    num_words = len(word_spl) # we are getting the  length of all of  words
    for i in word_spl:
        sum = sum + len(i) # we are looping through them to count the words

    print(sum/num_words)


def pig_latin():
    sentence = input(" enter the sentence to convert to pig latin") # we are asking the  the user for sentence input
    sent_spl = sentence.split() # we are splitting  the word by spaces
    for word in sent_spl: # for loop
        print(word[1:len(sentence)] + sentence[0] + "ay", end=" ") # for the lenth of the world we only want to takout the end portion and then add ay to it


if __name__ == '__main__':
