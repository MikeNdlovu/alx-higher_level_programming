#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        c, d = 0, 0
        a, b = tuple_a

    elif len(tuple_b) == 1:
        d = 0
        c = tuple_b[0]
        a, b = tuple_a

    else:
        a, b = tuple_a
        c, d = tuple_b
    sum1 = int(a) + int(c)
    sum2 = int(b) + int(d)
    tuple_c = (sum1, sum2)
    return tuple_c
