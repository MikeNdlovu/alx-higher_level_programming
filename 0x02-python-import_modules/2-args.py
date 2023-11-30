#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    str = []
    num = 0
    for i in sys.argv:
        str.append(i)
        num += 1
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))
    num = 1
    for i in str[num:]:
        print("{}: {}".format(num, i))
        num += 1
