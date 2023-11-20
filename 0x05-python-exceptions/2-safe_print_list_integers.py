#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    index = 0
    while (index < x):
        try:
            print("{:d}".format(my_list[index]), end="")
            index += 1
            i += 1
        except IndexError as err:
            raise
            print("{}".format("IndexError: list index out of range"))
            return
        except Exception:
            index += 1
            continue
    print()
    return (i)
