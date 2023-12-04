#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_i = 0
        for i in my_list:
            if max_i < int(i):
                max_i = int(i)
        return max_i
