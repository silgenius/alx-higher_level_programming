#!/usr/bin/python3

def is_same_class(obj, a_class):
    if a_class == object:
        return False
    return isinstance(obj, a_class)
