#!/usr/bin/python3

"""
A program that imports functions from calculator_1.py and
performs basic operations.

Usage: ./100-my_calculator.py <a> <operator> <b>

Arguments:
    a: First operand
    operator: The operation to perform (+, -, *, /)
    b: Second operand

If the number of arguments is not 3, the program prints:
    Usage: ./100-my_calculator.py <a> <operator> <b> followed by a new line
    and exits with the value 1.

If the operator is not one of the specified operators, the program prints:
    Unknown operator. Available operators: +, -, * and / followed by a new line
    and exits with the value 1.

    Example:
    $ ./100-my_calculator.py 10 + 5
    10 + 5 = 15
"""

from calculator_1 import add, sub, mul, div
from sys import exit, argv


def calculation():
    if len(argv) - 1 != 3:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    operator = ""
    for i in ['+', '-', '*', '/']:
        if i == argv[2]:
            operator = i
            break
    if operator == "":
        print("{}".format("Unknown operator. Available\
 operators: +, -, * and /"))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if operator == '+':
        print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    else:
        print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))


if __name__ == "__main__":
    calculation()
