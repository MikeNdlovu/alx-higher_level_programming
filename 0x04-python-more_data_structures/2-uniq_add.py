#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum1 = 0
    num = 0
    for i in my_list:
        if my_list.count(i) != 1:
            del my_list[num]
            num += 1
        else:
            num += 1
    for ints in my_list:
        sum1 += ints
    return sum1
