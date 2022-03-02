"""Faith Kelley
Lab7.py
 today we are opening and closing files
  I certify i am the only person that is  working on this project"""


def weighted_average(in_file_name, out_file_name):
    with open(in_file_name, 'r') as grade_file:
        with open(out_file_name, 'w') as average_file:
            grades = grade_file.readlines()
            for line in grades:
                grade_r = line.split(":")
                line_g = grade_r[1].strip()
                line_d = line_g.split(" ")
                for i in range(len(line_d)):
                    line_b = str(line_d[0:i:2]).strip(" ")
                    for l in range(len(line_d)):
                        line_h = str(line_d[1:l + 1:2]).strip(" ")

                print(line_b, line_h)
