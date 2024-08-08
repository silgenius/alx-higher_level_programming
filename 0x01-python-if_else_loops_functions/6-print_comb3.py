#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if i >= j:
            continue
        if (i == 8 and j == 9):
            break
        print("{}{}".format(i, j), end=", ")
print("{}".format(89))
