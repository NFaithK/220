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
        file_read = in_file.readline()
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
        i = i + 1
    return correct


# 4/20

def selection_sort(values):
    value = 0
    for i in range(len(values)):
        min_v = i
        for j in range(i + 1, len(values)):
            if values[min_v] > values[j]:
                min_v = j


def calc_area(rect):
    x_point_1 = rect.getP1()
    x_point_2 = rect.getP2()
    y_point_1 = rect.getp1()
    y_point_2 = rect.getp2()
    sub_x = abs(x_point_2 - x_point_1)
    sub_y = abs(y_point_2 - y_point_1)
    multiply = sub_x * sub_y
    print(multiply)


def rect_sort(rectangles):
    rectangle = 0
    while rectangle < len(rectangles):
        min = rectangle
        for i in range(rectangle, len(rectangles)):
            if calc_area(rectangles[i]) < calc_area(rectangles[min]):
                min = 1
                rectangles[min], rectangles[rectangle] = rectangles[rectangle], rectangles[min]
