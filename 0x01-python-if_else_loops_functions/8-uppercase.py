#!/usr/bin/python3
def uppercase(string):
    for char in string:
        upper_char = chr(ord(char) - 32)
        print("{}".format(upper_char), end='')
    print()

