#!/usr/bin/python3

"""
stats_script.py - Script to compute metrics from input lines
and print statistics.

This script reads input lines from stdin, where each line has the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys


def print_statistics(total_size, status_dict={}):
    print("File size: {:d}".format(total_size))
    for code in sorted(status_dict):
        count = status_dict[code]
        if count > 0:
            print("{:d}: {:d}".format(code, count))


my_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0

try:
    for i, line in enumerate(sys.stdin, start = 1):
        try:
            word = line.split()
            file_size = int(word[-1])
            status_code = int(word[-2])
        except (ValueError, IndexError):
            pass
        else:
            total_size += file_size
            my_dict[status_code] += 1


        if i % 10 == 0:
            print_statistics(total_size, my_dict)

except KeyboardInterrupt:
    print_statistics(total_size, my_dict)
    sys.exit(0)
