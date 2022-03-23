"""
Name: <your name goes here – Faith Kelley>
<Hw 7>.py

Problem: <we are opening and closing files an.>

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: <brooke duvall>
"""
from encryption import *

def number_words(in_file_name, out_file_name):
    file = open(in_file_name, 'r')
    data = file.read()
    data_split = data.split()
    out_file = open(out_file_name,'w')
    a = 1
    for i in data_split:
        out_file.write(str(a)+" " + i+"\n")
    out_file.close()
    file.close()



def hourly_wages(in_file_name, out_file_name):
    new_file = open(in_file_name, 'r') # you are reading  from this file
    new_file_r = new_file.read() # reading the  new file
    out_file = open(out_file_name, 'a') # we are appending the new file
    content = new_file_r.split("\n")  # we are using the  new line character for  the split method
    for line in content: # for loop
        line_content = line.split() # we are splitting the  line by spaces
        wage = eval(line_content[2]) # we are evaling the  line content  that we  indexed
        hours = eval(line_content[3]) # we are  evaling the line content we pulled from the
        pay = str((wage * hours)+(1.65 * hours))
        out_file.write(line_content[0] + " " + " " + line_content[1] + " " + " "+pay)
    new_file.close()
    out_file.close()


def calc_check_sum(isbn):
    acc = 0
    isbn_r = isbn.replace("-","")
    for i in range(10):
        isbn_v = eval(isbn_r[9-i])
        acc = acc+(i+1) * isbn_v
    return int(acc)




def send_message(file_name, friend_name):
    friend = open(file_name, 'r')
    text = friend.read()
    new_file = open(friend_name + ".txt", "w")
    new_file.write(text)


def send_safe_message(file_name, friend_name, key):
    encode_file = open(file_name,"r")
    encode_e = encode_file.read()
    content = encode_e.split("\n")
    new_file = open(friend_name + ".txt", 'a')
    for i in content:
        encoded = encode(i, key)
        new_file.write(encoded + "\n")
    encode_file.close()
    new_file.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    new_file = open(file_name, "r")
    message = new_file.read()
    key_file = open(file_name, 'r')
    key = key_file.read()
    message_split = message.split()
    for i in message_split:
        encode_better(i, key, friend_name + ".txt")
    new_file.close()
    key_file.close()



if __name__ == '__main__':
    pass
