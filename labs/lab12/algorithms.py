"""Faith Kelley
Algorithms. py
I  certify that i am the only one doing this project"""


def read_data(file_name):
    in_file = open(file_name, 'r')
    list = []
    file_read = in_file.readlines()
    while file_read:
        replace_line = list.replace("\n", "")
        replace_line_2 = replace_line.split(' ')
        i = 0
        second_line = []
        while i < len(replace_line_2):
            eval_num = eval(replace_line_2[i])
            second_line.append(eval_num)
            i += i
        line_file = list + second_line
        file_read = in_file.readline()\
        file_read.close()
        return line_file


def is_in_linear(search_val, values):
    i = 0
    correct = False
    while i < len(search_val) and correct == False:
        if values[i] == search_val:
            correct = True
        else:
            correct = False
        i = i+1
    return correct

