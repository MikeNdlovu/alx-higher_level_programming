#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0 and len(tuple_a) == 2:
        c, d = 0, 0
        a, b = tuple_a
    elif len(tuple_b) == 0 and len(tuple_a) == 1:
        c, b, d = 0, 0, 0
        a = tuple_a[0]
    elif len(tuple_b) == 0 and len(tuple_a) == 0:
        c, b, d, a = 0, 0, 0, 0
    elif len(tuple_b) == 1 and len(tuple_a) == 1:
        d, b = 0, 0
        c = tuple_b[0]
        a = tuple_a[0]
    elif len(tuple_b) == 1 and len(tuple_a) == 0:
        d, a, b = 0, 0, 0
        c = tuple_b[0]
    elif len(tuple_b) == 1 and len(tuple_a) == 2:
        d = 0
        c = tuple_b[0]
        a, b = tuple_a
    elif len(tuple_b) == 2 and len(tuple_a) == 1:
        c, d = tuple_b
        a = tuple_a[0]
        b = 0
    elif len(tuple_b) == 2 and len(tuple_a) == 0:
        c, d = tuple_b
        a, b = 0, 0
    else:
        a, b = tuple_a
        c, d = tuple_b
    sum1 = int(a) + int(c)
    sum2 = int(b) + int(d)
    tuple_c = (sum1, sum2)
    return tuple_c
