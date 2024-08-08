#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return (0)
    result, value = 0, 0
    for tup in my_list:
        result += tup[0] * tup[1]
        value += tup[1]
    return (result / value)
