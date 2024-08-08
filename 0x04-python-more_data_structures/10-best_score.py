#!/usr/bin/python3

def best_score(a_dictionary):
    high_score = 0

    if not a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > high_score:
            high_score = a_dictionary[key]
            name = key
    return (name)
