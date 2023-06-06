#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
unite = abs(number) % 10
if number < 0:
    unite = -unite
if int(unite) > 5:
    print("Last digit of", number, "is", unite, "and is greater than 5")
elif int(unite) == 0:
    print("Last digit of", number, "is", unite, "and is 0")
elif int(unite) < 6 and not 0:
    print("Last digit of", number, "is", unite, "and is less than 6 and not 0")
