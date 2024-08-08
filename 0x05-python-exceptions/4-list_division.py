#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while (i < list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("{}".format("wrong type"))
            new_list += [0]
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            new_list += [0]
        except IndexError:
            print("{}".format("out of range"))
            new_list += [0]
        else:
            new_list.append(result)
        finally:
            i += 1
    return (new_list)
