#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for item in my_list[0:x]:
            print("{}".format(item), end="")
            num += 1

    except:
        print("can't print")

    finally:
        print("")
    return (num)
