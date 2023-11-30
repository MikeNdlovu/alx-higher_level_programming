#!/usr/bin/python3
with open("hidden_4.pyc", 'r', errors='ignore') as file:
    content = file.read()
    a = content[225:245]
    print("{}".format(a))
    b = content[325:340]
    print("{}".format(b))
    c = content[418:430]
    print("{}".format(c))
