#!/usr/bin/python3

def my_function():
    for i in range(5):
        print(i)

# Disassemble the bytecode
import dis
dis.dis(my_function)

