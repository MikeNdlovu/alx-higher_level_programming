#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list) or idx < 0:
        return my_list
    else:
        n = 0
        new_list = []
        while n < len(my_list):
            if n == idx:
                n = idx + 1
            new_list.append(my_list[n])
            n += 1
        my_list = new_list
        return my_list
