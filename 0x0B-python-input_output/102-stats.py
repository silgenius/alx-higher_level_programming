#!/usr/bin/python3

"""
stats_script.py - Script to compute metrics from input lines
and print statistics.

This script reads input lines from stdin, where each line has the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys


def print_statistics(total_size, status_count):
    """
    printf module
    """
    print(f"File size: {total_size}")
    for code in sorted(status_count):
        count = status_count[code]
        if count > 0:
            print(f"{code}: {count}")

def main():
    """
    for the ,ain
    """

    total_size = 0
    status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            try:
                parts = line.split()
                file_size = int(parts[-1])
                status_code = int(parts[-2])
            except (ValueError, IndexError):
                # Skip invalid lines
                continue

            total_size += file_size
            status_count[status_code] += 1

            if line_number % 10 == 0:
                print_statistics(total_size, status_count)

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (Ctrl+C)
        print_statistics(total_size, status_count)

if __name__ == "__main__":
    main()

