#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < len(my_list) and idx > 0:
        my_list = my_list[idx]
        return my_list
    else:
        return None
