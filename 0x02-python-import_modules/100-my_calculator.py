#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    argc = len(sys.argv)
    operator = ["+", "-", "*", "/"]
    if (argc != 4):
        print("Usage: <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == operator[0]:
            print("{} {} {} = {}".format(a, operator[0], b, a + b))
        elif sys.argv[2] == operator[1]:
            print("{} {} {} = {}".format(a, operator[1], b, a - b))
        elif sys.argv[2] == operator[2]:
            print("{} {} {} = {}".format(a, operator[2], b, a * b))
        elif sys.argv[2] == operator[3]:
            print("{} {} {} = {}".format(a, operator[3], b, a / b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
