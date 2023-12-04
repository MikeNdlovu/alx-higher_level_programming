#!/usr/bin/python3
def no_c(my_string):
    remove = str.maketrans({"c":"", "C":""})
    my_string = my_string.translate(remove)
    return my_string
