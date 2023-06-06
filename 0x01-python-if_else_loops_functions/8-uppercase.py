#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:s}".format(chr(ord(char) & 0xdf)), end="")
    print()
