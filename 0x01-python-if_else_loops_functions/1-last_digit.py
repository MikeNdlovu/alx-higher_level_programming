#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number % 10 == 0:
    print(f"Last digit of {number} is 0 and is 0")

elif number > 0:
    num = number % 10
    if num > 5:
        print(f"Last digit of {number} is {num} and is greater than 5")
    elif num < 6:
        print(f"Last digit of {number} is {num} and is less than 6 and not 0")

else:
    num = (((number * -1) % 10) * -1)
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
