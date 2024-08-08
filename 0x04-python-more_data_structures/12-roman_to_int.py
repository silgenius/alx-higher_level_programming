#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result = 0
    prev_value = 0

    for char in roman_string:
        if char not in roman_numerals:
            return 0

        current_value = roman_numerals[char]

        if current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value

        prev_value = current_value

    return result
