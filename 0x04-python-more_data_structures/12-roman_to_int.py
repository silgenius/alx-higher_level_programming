#!/usr/bin/python3

def roman_to_int(roman_string):
    my_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result = 0

    if not roman_string:
        return (None)
    for alpha in roman_string:
        if alpha in my_dict:
            if result >= my_dict[alpha]:
                result += my_dict[alpha]
            else:
                result = my_dict[alpha] - result
        else:
            return (None)
    return (result)
