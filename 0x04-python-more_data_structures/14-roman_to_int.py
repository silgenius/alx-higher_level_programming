#!/usr/bin/python3

def roman_to_int(roman_string):
    my_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result = 0
    cal = 0
    x = 0
    if not roman_string:
        return (0)
    for alpha in roman_string:
        if alpha in my_dict:
            if x == 1:
                if my_dict[prev] < my_dict[alpha]:
                    cal = -1 * my_dict[prev]
                else:
                    cal = my_dict[prev]
            result += cal
            prev = alpha
            x = 1
        else:
            return (0)
    result += my_dict[alpha]
    return (result)
