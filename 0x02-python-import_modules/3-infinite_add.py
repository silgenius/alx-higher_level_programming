#!/usr/bin/python3

from sys import argv


def calculation():
    result = 0
    for arg in argv[1:]:
        result += int(arg)
    print("{}".format(result))


if __name__ == "__main__":
    calculation()
