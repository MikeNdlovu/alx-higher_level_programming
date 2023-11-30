#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = []
    for i in sys.argv:
        add.append(i)
    num = 1
    result = 0
    for i in add[num:]:
        result += int(add[num])
        num += 1
    print("{}".format(result))
