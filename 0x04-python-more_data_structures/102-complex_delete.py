#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    my_list = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            my_list.append(key)
    for i in my_list:
        del a_dictionary[i]
    return (a_dictionary)
