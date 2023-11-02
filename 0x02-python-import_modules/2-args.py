#!/usr/bin/python3

from sys import argv

print("{:d} {}".format(len(argv) - 1, "argu\
ment" if (len(argv) - 1) == 1 else "arguments"), end="")
print(":" if len(argv) - 1 > 0 else ".")
for i, arg in enumerate(argv[1:], start=1):
    print("{:d}: ".format(i), end="")
    print("{}".format(arg))
