def trade_alert(file_name):
    file = file_name
    open_file = open(file, 'r')
    content = open_file.read()
    file_split = content.split(" ")
    for i in range(len(file_split)):
        if int(file_split[i]) > 830:
            print("This Trading volume exceeds 830 at {}".format(i + 1))
        elif (file_split[i]) == 500:
            print("This trading  volume is equal to 500 at {}".format(i + 1))
    file.close()



