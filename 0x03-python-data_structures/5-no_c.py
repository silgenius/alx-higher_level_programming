#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for alpha in my_string:
        if (alpha == 'C' or alpha == 'c'):
            continue
        new_str += alpha
    return (new_str)
