#!/usr/bin/python3

import sys
from collections import defaultdict

def process_line(line, status_counts, total_size):
    # Parse the line and update metrics
    parts = line.split()
    status_code = parts[-2]
    file_size = int(parts[-1])
    
    total_size += file_size
    status_counts[status_code] += 1
    
    return total_size

def print_statistics(total_size, status_counts):
    # Print total file size
    print(f"File size: {total_size}")

    # Print number of lines by status code in ascending order
    for code in sorted(status_counts):
        count = status_counts[code]
        print(f"{code}: {count}")

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_counter = 0

    try:
        for line in sys.stdin:
            total_size = process_line(line, status_counts, total_size)
            line_counter += 1

            if line_counter % 10 == 0:
                print_statistics(total_size, status_counts)
                line_counter = 0

    except KeyboardInterrupt:
        # Handle CTRL + C interruption
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()

