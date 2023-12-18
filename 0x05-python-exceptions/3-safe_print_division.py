#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a/b
        return div
    except ZeroDivisionError:
        return None
    finally:
        try:
            print("Inside result: {}".format(div))
        except ZeroDivisionError:
            print("Inside result: {}".format(None))
