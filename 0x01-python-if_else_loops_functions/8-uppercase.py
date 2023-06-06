#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:s}".format(chr(ord(char) - 32)), end="")
        else:
            print(char, end="")
