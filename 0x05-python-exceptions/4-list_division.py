#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    num = 0
    store = []
    while num < list_length:
        try:
            div = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            num += 1
            store.append(div)
    return store
