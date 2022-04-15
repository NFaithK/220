# searching sorting and recursion
# linear search- going through the  list using each index until you find the number or if you dont find it, it will end to do none


def linear_search(search_list, target):
    i = 0
    while i < len(search_list):
        if target == search_list[i]:
            return 1
        else:
            i += 1
    return -1


if __name__ == '__main__':
    my_list = [3, 6, 1, 4, 6, 34, 95, 12]
    target = 7
    result = linear_search(my_list, target)
    if result >= 0:
        print(result)
    else:
        print("nope!")
# target in <variable> is another way to do this
