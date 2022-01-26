"""
Faith Kelley,
lab2.py
today we are trying to find the rms average, harmonic average and the geometric average  ,
i certify that i am the only  one   doing this work"""
import math


def means():
    rms_acc = 0
    hm_acc = 0
    gm_acc = 1
    total_value = eval(input("Enter the values to be entered:"))
    for i in range(total_value):
        value = eval(input("enter value: "))
        rms_acc = value ** 2 + rms_acc
        hm_acc = 1/value + hm_acc
        gm_acc = value * gm_acc
    rms_s = rms_acc / total_value
    rms_s = math.sqrt(rms_s)
    rms_s = round(rms_s, 3)
    hm_s = total_value/hm_acc
    gm_s = math.sqrt(gm_acc)
    gm_s = math.sqrt(gm_s)
    gm_s = round(gm_s, 3)
    print(rms_s)
    print(hm_s)
    print(gm_s)
