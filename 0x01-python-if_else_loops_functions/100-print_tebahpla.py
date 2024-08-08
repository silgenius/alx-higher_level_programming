#!/usr/bin/python3

i = ord('Z')
while i >= ord('A'):
    if (i % 2 == 0):
        i += 32
    print("{}".format(chr(i)), end="")
    if (i > ord('a')):
        i -= 32
    i -= 1
