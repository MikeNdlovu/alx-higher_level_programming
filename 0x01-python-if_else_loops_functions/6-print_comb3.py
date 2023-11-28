#!/usr/bin/python3
for i in range(0, 8):
    for n in range(0, 10):
        if n > i:
            print("{}{}".format(i, n), end=", ")

print("{}{}".format(i + 1, n))
